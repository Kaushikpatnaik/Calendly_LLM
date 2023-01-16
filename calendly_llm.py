"""
Calendly LLM agent

We want the LLM to be a calendly agent. So essentialy the LLM has three pieces of work:

1. NLI i.e taking the natural language request and retrieving important parameters like meeeting invitees, time, date etc
2. Ask follow up questions until all necessary information to complete a request id one
3. Act as a planner/agent to write code to complete the actions
"""
from collections import defaultdict

from llm_modules.self_heal import self_heal
from llm_modules.follow_up import follow_up_iterative
from llm_modules.prompt_templates import *
from llm_utils import get_response
from evaluation.evaluation import all_info_create_test_cases, all_info_edit_test_cases

FOLLOW_UP_COT_PROMPT_TEMPLATE = follow_up_prompt_w_cot
COT_PROMPT_TEMPLATE = prompt_w_few_shot_examples

outputs = defaultdict(dict)
for query in all_info_create_test_cases:
    updated_query, request_type = follow_up_iterative(query, 3, prompt_template=FOLLOW_UP_COT_PROMPT_TEMPLATE)

    updated_query += " . Request type is "+request_type

    codegen_prompt = COT_PROMPT_TEMPLATE.format(query=updated_query)
    output = get_response(
        prompt=codegen_prompt, engine="text-davinci-003", temperature=0, max_tokens=1600
    )

    upd_output, code_exec_status = self_heal(output, num_retries=2)

    outputs[query]["code_output"] = upd_output
    outputs[query]["code_exec"] = code_exec_status

for k, v in outputs.items():
    print(k)
    for k1, v1 in v.items():
        if k1 in ["code_exec"]:
            print(v1)

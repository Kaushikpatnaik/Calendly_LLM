"""
Calendly LLM agent

We want the LLM to be a calendly agent. So essentialy the LLM has three pieces of work:

1. NLI i.e taking the natural language request and retrieving important parameters like meeeting invitees, time, date etc
2. Ask follow up questions until all necessary information to complete a request id one
3. Act as a planner/agent to write code to complete the actions
"""
from collections import defaultdict

from self_heal import self_heal
from prompt_templates import *
from llm_utils import get_response
from evaluation import all_info_create_test_cases, all_info_edit_test_cases

PROMPT_TEMPLATE = prompt_w_few_shot_examples

outputs = defaultdict(dict)
for query in all_info_create_test_cases:
    curr_prompt = PROMPT_TEMPLATE.format(query=query)
    output = get_response(prompt=curr_prompt, engine="text-davinci-003", temperature=0, max_tokens=1600)
    
    upd_output, code_exec_status = self_heal(output, num_retries=2)

    outputs[query]['code_output'] = upd_output
    outputs[query]['code_exec'] = code_exec_status

for k, v in outputs.items():
    print(k)
    for k1, v1 in v.items():
        if k1 in ['code_exec']:
            print(v1)


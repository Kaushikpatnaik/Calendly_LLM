"""
Calendly LLM agent

We want the LLM to be a calendly agent. So essentialy the LLM has three pieces of work:

1. NLI i.e taking the natural language request and retrieving important parameters like meeeting invitees, time, date etc
2. Ask follow up questions until all necessary information to complete a request id one
3. Act as a planner/agent to write code to complete the actions
4. Self-heal code
"""
import os
import json
from collections import defaultdict
from datetime import datetime
from typing import Sequence, Union

from tqdm import tqdm

from llm_modules.self_heal import self_heal
from llm_modules.follow_up import follow_up_iterative
from llm_modules.prompt_templates import *
from llm_utils import get_response
from evaluation.test_cases import *

FOLLOW_UP_COT_PROMPT_TEMPLATE = follow_up_prompt_w_cot
COT_PROMPT_TEMPLATE = prompt_w_few_shot_examples


def run_calendly(
    query: Union[str, Sequence[str]],
    engine: str = "text-davinci-003",
    follow_up_retries: int = 3,
    self_heal_retries: int = 2,
):
    updated_query, request_type, num_attempts = follow_up_iterative(
        query, follow_up_retries, engine, prompt_template=FOLLOW_UP_COT_PROMPT_TEMPLATE
    )

    updated_query += " Request type is " + request_type + "."

    codegen_prompt = COT_PROMPT_TEMPLATE.format(query=updated_query)
    output = get_response(
        prompt=codegen_prompt, engine=engine, temperature=0, max_tokens=1600
    )

    upd_output, code_exec_status, returned_value = self_heal(
        output, self_heal_retries, engine
    )

    return upd_output, code_exec_status, returned_value


def run_test_cases(test_cases: Sequence[str], test_case_name: str):
    outputs = defaultdict(dict)
    for query in tqdm(test_cases):
        if isinstance(query, str):
            upd_output, code_exec_status, returned_value = run_calendly([query])
        else:
            upd_output, code_exec_status, returned_value = run_calendly(query)

        outputs[query]["code_output"] = upd_output
        outputs[query]["code_exec"] = code_exec_status
        outputs[query]["returned_value"] = returned_value

    # write output to file
    now = datetime.now()
    file_name = test_case_name + "_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".json"

    with open(os.path.join(".", "logging", file_name), "w") as f:
        json.dump(outputs, f)

    return outputs


if __name__ == "__main__":
    all_info_output = run_test_cases(all_info_create_test_cases, "all_info_create")
    
    #run_test_cases(all_info_edit_test_cases, "all_info_edit")
    #run_test_cases(all_info_find_test_cases, "all_info_find")
    #run_test_cases(follow_up_test_cases, "follow_up")

"""
Query is first sent to follow-up module

- module ascertains if current query meets all the requirements for creating or editing a calendar invite
- if not it creates list of follow-up questions
- creates a composed follow-up question
- user is asked the follow-up question
- this is repeated for x times, after which the program exits as there is not info to do anything
- if requirements are satisfied then
"""

from llm_modules.prompt_templates import *
from llm_utils import get_response

FOLLOW_UP_COT_PROMPT_TEMPLATE = follow_up_prompt_w_cot

def follow_up_iterative(init_requests, num_retries, prompt_template=FOLLOW_UP_COT_PROMPT_TEMPLATE):
    # for testing purposes init_requests is a list of user requests
    attempts = 0
    cp_request = init_requests[attempts]
    while attempts < num_retries:
        curr_prompt = prompt_template + cp_request
        follow_up_dict = get_response(
            prompt=curr_prompt, engine="text-davinci-003", temperature=0, max_tokens=256
        )
        follow_up_dict = eval(follow_up_dict)
        attempts += 1
        if follow_up_dict["follow_up_condensed"] == 'No follow up questions needed.' or attempts == num_retries:
            return follow_up_dict["request"], follow_up_dict["request_type"]
        else:
            q_to_user = follow_up_dict["follow_up_condensed"]
            cp_request += " " + init_requests[attempts]
    return follow_up_dict["request"], follow_up_dict["request_type"]


if __name__ == "__main__":
    from evaluation.evaluation import follow_up_test_cases

    for test_case in follow_up_test_cases:
        final_request, request_type = follow_up_iterative(test_case, len(test_case))
        print(final_request, request_type)

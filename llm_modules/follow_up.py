"""
Query is first sent to follow-up module

- module ascertains if current query meets all the requirements for creating or editing a calendar invite
- if not it creates list of follow-up questions
- creates a composed follow-up question
- user is asked the follow-up question
- this is repeated for x times, after which the program exits as there is not info to do anything
- if requirements are satisfied then
"""
import copy
from llm_modules.prompt_templates import *
from llm_utils import get_response

FOLLOW_UP_COT_PROMPT_TEMPLATE = follow_up_prompt_w_cot

def follow_up_iterative(init_requests, num_retries, prompt_template=FOLLOW_UP_COT_PROMPT_TEMPLATE):
    # for testing purposes init_requests is a list of user requests
    attempts = 0
    cp_request = init_requests[attempts]
    while attempts < num_retries:
        attempts += 1
        curr_prompt = prompt_template + cp_request
        print(attempts, cp_request)
        print(curr_prompt)
        follow_up_dict = get_response(
            prompt=curr_prompt, engine="text-davinci-003", temperature=0, max_tokens=256
        )
        print(follow_up_dict)
        follow_up_dict = eval(follow_up_dict)
        if follow_up_dict["follow_up_condensed"] == 'No follow up questions needed.':
            return follow_up_dict["request"]
        else:
            q_to_user = follow_up_dict["follow_up_condensed"]
            cp_request += " " + init_requests[attempts]
            print(attempts, cp_request)
    return follow_up_dict["request"], follow_up_dict["request_type"]


if __name__ == "__main__":
    final_request = follow_up_iterative(
        [
            "Book a meeting.",
            "Invite Glenn, Shreyas, and Sameer to a 1hr meeting at 2:30pm.",
            "Set the meeting date to next tuesday. Meeting agenda is to discuss 2023 plans.",
        ],
        4,
    )
    assert (
        final_request
        == "Book a meeting. Invite Glenn, Shreyas, and Sameer to a 1hr meeting at 2:30pm. Set the meeting date to next tuesday. Meeting agenda is to discuss 2023 plans."
    )

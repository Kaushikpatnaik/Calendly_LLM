'''
Query is first sent to follow-up module

- module ascertains if current query meets all the requirements for creating or editing a calendar invite
- if not it creates list of follow-up questions
- creates a composed follow-up question
- user is asked the follow-up question
- this is repeated for x times, after which the program exits as there is not info to do anything
- if requirements are satisfied then
'''
import copy
from prompt_templates import *
from llm_utils import get_response

def follow_up_iterative(init_requests, num_retries):
    # for testing purposes init_requests is a list of user requests
    attempts = 0
    cp_request = copy.deepcopy(init_requests[attempts])
    while attempts < num_retries:
        attempts += 1
        curr_prompt = follow_up_prompt.format(query=cp_request)
        follow_up_dict = get_response(prompt=curr_prompt, engine="text-davinci-003", temperature=0, max_tokens=256)
        if follow_up_dict["follow_up_condensed"] == "":
            return follow_up_dict["request"]
        else:
            q_to_user = follow_up_dict["follow_up_condensed"]
            cp_request += " " + copy.deepcopy(init_requests[attempts])
    return follow_up_dict["request"]
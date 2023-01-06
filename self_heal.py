'''
Take output from llm, run exec
Pass in code + output error to llm for edits
'''
import copy
from prompt_templates import *
from llm_utils import get_response

def self_heal(program_string, num_retries):
    attempts = 0
    cp_program_string = copy.deepcopy(program_string)
    prog_exec_success = False
    while attempts < num_retries:
        try:
            output = exec(cp_program_string)
            prog_exec_success = True
            break
        except Exception as e:
            attempts += 1
            curr_prompt = self_heal_prompt.format(program=cp_program_string, error=e)
            output = get_response(prompt=curr_prompt, engine="text-davinci-003", temperature=0, max_tokens=1600)
            cp_program_string = copy.deepcopy(output)
    return output, prog_exec_success

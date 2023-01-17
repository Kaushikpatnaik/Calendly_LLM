"""
Take output from llm, run exec
Pass in code + output error to llm for edits
"""
import copy
from llm_modules.prompt_templates import *
from llm_utils import get_response


def self_heal(program_string, num_retries):
    attempts = 0
    cp_program_string = copy.deepcopy(program_string)
    while attempts < num_retries:
        try:
            exec(cp_program_string)
            returned_val = return_output()
            return cp_program_string, True, returned_val
        except Exception as e:
            attempts += 1
            curr_prompt = self_heal_prompt.format(program=cp_program_string, error=e)
            cp_program_string = get_response(
                prompt=curr_prompt,
                engine="text-davinci-003",
                temperature=0,
                max_tokens=1600,
            )
    return cp_program_string, False, None

if __name__ == "__main__":
    wrong_code = """
    from provided_api import *
# lowercase names and meeting agenda
meeting_summary = ""Pickup my parents"".lower()
    """
    correct_code = """

from provided_api import *

# lowercase names and meeting agenda
meeting_summary = "Pickup my parents".lower()
    """

    corrected_code, is_correct = self_heal(wrong_code, 3)
    assert is_correct
    assert correct_code.split() == corrected_code.split()

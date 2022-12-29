import re
import json

class PromptTemplate():
    """
    Schema to represent a prompt for LLM. Copy from Langchain with some changes
    """
    def __init__(self, template) -> None:
        super().__init__()
        self.template = template

        # parse the template to identify variables
        res = re.findall(r'\{.*?\}', template)
        self.variables = {k[1:-1]:None for k in res}

    def format(self, input_variables):
        # input variables must be passed as dict
        return self.template.format(**input_variables)


def load_prompt_template_json(prompt_json):
    with open(prompt_json, 'r') as f:
        data = json.load(f)

    return data


def get_prompt_template_from_json(prompt_json ,key):
    data = load_prompt_template_json(prompt_json)
    return data[key]
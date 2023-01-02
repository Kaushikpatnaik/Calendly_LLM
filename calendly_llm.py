"""
Calendly LLM agent

We want the LLM to be a calendly agent. So essentialy the LLM has three pieces of work:

1. NLI i.e taking the natural language request and retrieving important parameters like meeeting invitees, time, date etc
2. Ask follow up questions until all necessary information to complete a request id one
3. Act as a planner/agent to write code to complete the actions
"""
from collections import defaultdict

from langchain import LLMChain, OpenAI, PromptTemplate

from prompt_templates import prompt_w_api, prompt_wo_api, api_list_option, api_list_none
from evaluation import all_info_create_test_cases

PROMPT_TEMPLATE = prompt_w_api

llm = OpenAI(model_name= "text-davinci-003", temperature=0, max_tokens=1600)
prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["query"])
model_chain = LLMChain(llm=llm, prompt=prompt)

# load the mock api file for testing execution correctness
with open("provided_api.py") as file:
    api_content = file.read()

outputs = defaultdict(dict)
for req in all_info_create_test_cases:
    output = model_chain.run(req)
    outputs[req]['code_output'] = output
    outputs[req]['code_exec'] = False
    try:
        code_exec = exec(output)
        outputs[req]['code_exec'] = True
    except:
        continue

for k, v in outputs.items():
    print(k)
    for k1, v1 in v.items():
        print(v1)


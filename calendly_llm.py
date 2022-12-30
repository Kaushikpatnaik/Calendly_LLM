"""
Calendly LLM agent

We want the LLM to be a calendly agent. So essentialy the LLM has three pieces of work:

1. NLI i.e taking the natural language request and retrieving important parameters like meeeting invitees, time, date etc
2. Ask follow up questions until all necessary information to complete a request id one
3. Act as a planner/agent to write code to complete the actions
"""

prompt_w_api = f"""You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. {api_list_option}
Write code for completing the following request. Let's think step by step.""" + "{query}"

prompt_wo_api = """You are a calender assistant that takes in user instructions and creates, edits and updates google calendar. Write code for completing the following request. Let's think step by step.{query}"""

"""##### Specifying and running LLM chains"""

from langchain import LLMChain, OpenAI, HuggingFaceHub, PromptTemplate

llms = [
    (OpenAI(model_name= "code-cushman-001", temperature=0, max_tokens=1600), "code-cushman-001"),
    (OpenAI(model_name= "text-davinci-002", temperature=0, max_tokens=1600), "text-davinci-002"),
    (OpenAI(model_name= "text-davinci-003", temperature=0, max_tokens=1600), "text-davinci-003"),
    (OpenAI(model_name= "text-curie-001", temperature=0, max_tokens=1600), "text-curie-001"),
    (HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0}), "flan-t5-xl")
]

promptTemp1 = PromptTemplate(template=prompt_w_api, input_variables=["query"])
promptTemp2 = PromptTemplate(template=prompt_wo_api, input_variables=["query"])

model_chains_prompt_w_api = [(LLMChain(llm=llm, prompt=promptTemp1), name, llm._identifying_params) for llm, name in llms]
model_chains_prompt_wo_api = [(LLMChain(llm=llm, prompt=promptTemp2), name, llm._identifying_params) for llm, name in llms]

def run_model_chains(chains, query):
    chain_output = defaultdict(list)
    for chain, name, params in chains:
        output = chain.run(query)
        chain_output[query].append([name, params, output])
    return chain_output

preprend_python_api_code = ""

def get_op_exec_scores(result_dict):
    # For each parsed output run python exec and get scores
    exec_results = []
    for prompt, v in result_dict.items():
        for model_name, op in v.items():
            try:
                exec(op)
                exec_results.append([prompt, model_name, True])
            except:
                exec_results.append([prompt, model_name, False])
    return exec_results

for query in all_info_create_test_cases[:1]:
    w_api_prompt_op = run_model_chains(model_chains_prompt_w_api, query)
    wo_api_prompt_op = run_model_chains(model_chains_prompt_wo_api, query)

w_api_exp_results = format_model_chain_output(w_api_prompt_op)
wo_api_exp_results = format_model_chain_output(wo_api_prompt_op)

text_vs_code_comparison, rlhf_vs_sft_comparison, model_size_comparison, flan_vs_rlhf_comparison = w_api_exp_results

pretty_print_results(text_vs_code_comparison)
get_op_exec_scores(text_vs_code_comparison)
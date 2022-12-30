"""
Experiments

We are interested in how well the model execution changes with

*   Code models vs Text models
*   RLHF vs Supervised Fine-tuning (SFT)
*   Size of model
*   GPT-3 vs T5 + FLAN (i.e instructions finetuning)
*   Zero-shot vs Few-shot
*   Using pre-defined APIs vs writing code from scratch

The models being compared are 
*   code-cushman-001 (code-completion model)
*   text-davinci-002 (Supervised fine-tuning model based on code-davinci-002)
*   text-davinci-003 (RLHF + text-davinci-002)
*   text-curie-001 (smaller model of text-davinci-002)
*   Flan-T5-XL (from hugging facehub, trained using instruction tuning)

To get the experimental results, the following comparisons are made:
*   Code vs Text: code-cushman-001 vs text-curie-001
*   RLHF vs SFT: text-davinci-002 vs text-davinci-003
*   Size of model: text-davinci-002 vs text-curie-001
*   Flan vs RLHF: flan-t5-xl vs text-davinci-003

Prompting techniques will help determine the results the last two results

Given information above, we will essentially pass queries to the agent and the agent will attempt to complete the request. These 20 test cases are of varying difficulty and are primarily divided into cases which need follow-ups and those which dont

All code generated from the model is tested in a python interpreter for correctness. If there is any error, the task is assumed to be failed. 
For experiments where we use the API, we will pre-pend function definitions used in the API.
"""

from collections import defaultdict
# Formatting outputs from chains to map to experiments

pattern = r"\{([^}]*)\}"

def format_model_chain_output(input_dict):
    #Code vs Text: code-cushman-001 vs text-curie-001
    #RLHF vs SFT: text-davinci-002 vs text-davinci-003
    #Size of model: text-davinci-002 vs text-curie-001
    #Flan vs RLHF: flan-t5-xl vs text-davinci-003
    text_vs_code_comparison = defaultdict(dict)
    rlhf_vs_sft_comparison = defaultdict(dict)
    model_size_comparison = defaultdict(dict)
    flan_vs_rlhf_comparison = defaultdict(dict)

    # LangChain really messes up the outputs
    for k, v in input_dict.items():
        model_name = k
        parsed_output, input_prompt, model_params = v

        if model_name == "code-cushman-001":
            text_vs_code_comparison[input_prompt][model_name] = parsed_output
        if model_name == "text-curie-001":
            text_vs_code_comparison[input_prompt][model_name] = parsed_output
            model_size_comparison[input_prompt][model_name] = parsed_output
        if model_name == "text-davinci-002":
            rlhf_vs_sft_comparison[input_prompt][model_name] = parsed_output
            model_size_comparison[input_prompt][model_name] = parsed_output
        if model_name == "text-davinci-003":
            rlhf_vs_sft_comparison[input_prompt][model_name] = parsed_output
        if model_name == "flan-t5-xl":
            flan_vs_rlhf_comparison[input_prompt][model_name] = parsed_output

    return text_vs_code_comparison, rlhf_vs_sft_comparison, model_size_comparison, flan_vs_rlhf_comparison
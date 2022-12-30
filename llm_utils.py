import os
import numpy as np

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def _find_generated_answer(tokens, newline="\n" ): 
    """LMs tend to insert initial newline characters before
    they begin generating text. This function ensures that we 
    properly capture the true first line as the answer while
    also ensuring that token probabilities are aligned."""        
    answer_token_indices = []
    char_seen = False            
    for i, tok in enumerate(tokens):
        # This is the main condition: a newline that isn't an initial
        # string of newlines:
        if tok == newline and char_seen:
            break
        # Keep the initial newlines for consistency:
        elif tok == newline and not char_seen:
            answer_token_indices.append(i)
        # Proper tokens:
        elif tok != newline:
            char_seen = True
            answer_token_indices.append(i)
    return answer_token_indices 

def get_response(prompt, engine="text-davinci-003", max_tokens=256, temperature=0, top_p=1, get_logits=False):
    response = openai.Completion.create(
        model=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=0,
        presence_penalty=0
    )

    # From here, we parse each example to get the values
    # we need:
    ex = response["choices"]
    tokens = ex["logprobs"]["tokens"]
    logprobs = ex["logprobs"]["token_logprobs"]        
    probs = list(np.exp(logprobs))
    if "<|endoftext|>" in tokens:
        end_i = tokens.index("<|endoftext|>")
        tokens = tokens[ : end_i]  # This leaves off the "<|endoftext|>"
        probs = probs[ : end_i]    # token -- perhaps dubious.
    ans_indices = _find_generated_answer(tokens)
    answer_tokens = [tokens[i] for i in ans_indices]
    answer_probs = [probs[i] for i in ans_indices]
    answer = "".join(answer_tokens)      

    if get_logits:
        data = {
            "prompt": prompt,
            "generated_text": ex["text"],
            "generated_tokens": tokens,
            "generated_probs": probs,
            "generated_answer": answer,
            "generated_answer_tokens": answer_tokens,
            "generated_answer_probs": answer_probs}

    else:
        data = {
            "prompt": prompt,
            "generated_text": ex["text"],
            "generated_answer": answer
        }
        
    return data

def pretty_print_langchain_results(result_dict):
    for prompt, v in result_dict.items():
        print(prompt)
        for model_name, op in v.items():
            print(model_name)
            print(op)



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

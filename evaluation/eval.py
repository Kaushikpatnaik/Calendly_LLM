'''
Code to test correctness of outputs from Calendly LLM
'''
from typing import Sequence
import json
from test_cases import *

def test_result_correctness(gts: Sequence[dict], preds: Sequence[dict], debug=True):
    json_correct_count = 0
    code_exec_count = 0
    for gt, pred in zip(gts, preds):
        pred_json = pred["returned_value"]
        if gt == pred_json:
            json_correct_count += 1
        else:
            if debug:
                print(pred["code_output"])
                for k in gt.keys():
                    if gt[k] != pred_json[k]:
                        print("Key: ", k, "Gt: ", gt[k], "Pred: ", pred_json[k])
        if pred["code_exec"]:
            code_exec_count += 1
    return code_exec_count, json_correct_count

if __name__ == "__main__":
    # load already run json
    basepath_str = "/home/dexter89_kp/Desktop/Projects/Calendly_LLM"
    with open("logging/all_info_create_2023-01-20_00-25-14.json", "r") as f:
        results = json.load(f)

    code_exec_res, json_correct_res = test_result_correctness(all_info_create_test_answers, results.values())
    print(code_exec_res, json_correct_res)

    
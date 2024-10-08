"""
Title: Evaluation Script for Schema generated by llama3 3b

Description:
This script is for evaluating all schemas based on hierarchical structure text 
generated by llama3 3b with regard to ground truth schemas.


Usage:
run command: python 3 eval_all_3b.py

"""
import json
import argparse
import os

def extract_relations(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    events = {event["@id"]: event["name"] for event in data["events"]}
    relations = []

    for relation in data.get("relations", []):
        relation_type = relation["wd_label"]
        subject_event_id = relation["relationSubject"]
        object_event_id = relation["relationObject"]
        subject_event_name = events.get(subject_event_id)
        object_event_name = events.get(object_event_id)
        importance_rate = 0 
        relations.append((subject_event_name, relation_type, importance_rate, object_event_name))
        
    for event in data.get("events", []):
        parent_event_id = event["@id"]
        parent_event_name = events.get(parent_event_id)
        for child in event.get("children", []):
            child_event_id = child["child"]
            child_event_name = events.get(child_event_id)
            importance_rate = child.get("importance", 0)
            relations.append((parent_event_name, "has_subevent", importance_rate, child_event_name))
        
    return relations

def evaluate_metrics(relations_file1, relations_file2, cnt):
    set_file1 = set(relations_file1)
    set_file2 = set(relations_file2)
    
    total_tuple_in_schema_generated = len(set_file1)
    total_tuple_in_ground_truth = len(set_file2)

    matching_tuples = set_file1.intersection(set_file2)
    number_of_matching_tuple = len(matching_tuples)
    #print("set1", set_file1)
    #print("set2", set_file2)

    precision = 0
    recall = 0
    f_score = 0

    if number_of_matching_tuple != 0:
        precision = number_of_matching_tuple / total_tuple_in_schema_generated
        recall = number_of_matching_tuple / total_tuple_in_ground_truth
        f_score = 2 * (precision * recall) / (precision + recall)
    
    print(f"Total number of tuples in schema generated: {total_tuple_in_schema_generated}")
    print(f"Total number of tuples in ground truth: {total_tuple_in_ground_truth}")
    
    print(f"Number of matching tuples: {number_of_matching_tuple}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F-Score: {f_score}")

    return {
        "total_tuple_in_schema_generated": total_tuple_in_schema_generated,
        "total_tuple_in_ground_truth": total_tuple_in_ground_truth,
        "number_of_matching_tuple": number_of_matching_tuple,
        "precision": precision,
        "recall": recall,
        "f_score": f_score
    }

def save_results(output_file, results):
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(results)

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
    

def main(dir_eval, dir_gt, output_file):
    cnt = 0
    precision_sum = 0
    recall_sum = 0
    f_score_sum = 0
    for filename in os.listdir(dir_eval):
        if filename.endswith(".json"):
            file_eval = os.path.join(dir_eval, filename)
            file_gt = os.path.join(dir_gt, filename.replace('_l3.json', 'R.json'))
            print(file_eval, file_gt)
            
            cnt += 1
            relations_file1 = extract_relations(file_eval)
            relations_file2 = extract_relations(file_gt)

            # Calculate and print metrics
            results = evaluate_metrics(relations_file1, relations_file2, cnt)
            precision_sum += results["precision"]
            recall_sum += results["recall"]
            f_score_sum += results["f_score"]
            #save_results(output_file, results)

    pre_ave = precision_sum / cnt
    rec_ave = recall_sum / cnt
    f_ave = f_score_sum / cnt
    print(pre_ave, rec_ave, f_ave)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_eval", default='../sdf_output_llama3_3b/', type=str)
    parser.add_argument("--dir_gt", default='ground_truth/academic/', type=str)
    parser.add_argument("--output_file", default='eval/result.json', type=str)

    args = parser.parse_args()

    main(args.dir_eval, args.dir_gt, args.output_file)


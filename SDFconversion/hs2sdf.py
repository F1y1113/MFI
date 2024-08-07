import json
from collections import defaultdict 
import argparse
import logging
import os

def main(paperID, input_hs, output_dir):
    
    with open(os.path.join(input_hs, paperID + '.txt'), 'r') as tex:
        text_con = tex.readlines()
        
    text_dict = defaultdict(list) 
    event_dict = defaultdict(list)

    cnt = 0
    text_dict['0'] = []
    for idx, item in enumerate(text_con):
        if item != '\n':
            text_dict[str(cnt)].append(item)
        else:
            cnt += 1
            
    for num in range(len(text_dict)):
        subNUM = text_dict[str(num)][0][0 : -1].lower().count("sub")
        ID = text_dict[str(num)][2][10 : -1].lower()
        des = text_dict[str(num)][3][13 : -1]
        name = text_dict[str(num)][1][7 + subNUM * 3 : -1]
        
        part = text_dict[str(num)][4][14 : -1].split(', ')
        new_part = []   
        if part[0] != 'xxxx':
            for idx in range(len(part)):
                new_part.append(part[idx].split(' ')[-1])
        
        if text_dict[str(num)][5][11 : -1] != 'xxxx':
            relation = text_dict[str(num)][5][11 : -1].split(', ')
        else:
            relation = []
            
        #event name
        event_dict[ID].append(name)
        #event description
        event_dict[ID].append(des)
        #event participants
        event_dict[ID].append(new_part)
        event_dict[ID].append(relation)

    schema_dict = {}
    schema_dict['@context'] = ["https://kairos-sdf.s3.amazonaws.com/context/kairos-v2.2.jsonld", {"cmu": "https://www.cmu.edu/"}]
    schema_dict['sdfVersion'] = "2.2"
    schema_dict['@id'] = paperID
    schema_dict['version'] = "v0"
    schema_dict['events'] = []
    schema_dict['relations'] = []
    schema_dict['entities'] = []
    schema_dict['privateData'] = {"inputDigest": []}
    schema_dict['provenanceData'] = []

    #schema_dict['events']

    for event in event_dict:
        single_event = {}
        single_event['@id'] = event
        single_event['name'] = event_dict[event][0]
        single_event['participants'] = []
        single_event['children'] = []
        
        if event_dict[event][2] != []:
            for even in event_dict[event][2]:
                child_dict = {}
                child_dict['child'] = even
                child_dict['importance'] = 1
                single_event['children'].append(child_dict)
            single_event['children_gate'] = 'and'
        
        single_event['wd_node'] = ''
        single_event['wd_label'] = event_dict[event][0]
        single_event['wd_description'] = event_dict[event][1]
        single_event['description'] = event_dict[event][1]
        single_event['privateData'] = {"originalDocumentId": ""}
        
        schema_dict['events'].append(single_event)
        

    #schema_dict['relations']
    for event in event_dict:
        if event_dict[event][3] != []:
            for re in range(len(event_dict[event][3])):
                single_relation = {}
                single_relation['@id'] = "cmu:Relations/00443/before"
                single_relation['wd_node'] = "wd:Q79030196"
                single_relation['wd_label'] = "before"
                single_relation['wd_description'] = "qualifies something (inception or end of a thing, event, or date) as happening previously to another thing"
                single_relation['relationSubject'] = event_dict[event][3][re].split('>')[0]
                single_relation['relationObject'] = event_dict[event][3][re].split('>')[1]
                single_relation['privateData'] = {"originalDocumentId": ""}
        
        schema_dict['relations'].append(single_relation)

    with open(output_dir + paperID + '.json', 'w') as fp:
        json.dump(schema_dict, fp)
        print(paperID + ' finish')

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ID", default=None, type=str, required=True)
    parser.add_argument("--input_dir", default='/home/aikes/SDFconversion/hs_txt', type=str)
    parser.add_argument("--output_dir", default='/home/aikes/SDFconversion/sdf_output/', type=str) 
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = _parse_args()
    
    logging.info("Start")
    main(args.ID, args.input_dir, args.output_dir)
    
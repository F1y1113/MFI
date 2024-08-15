import json
from collections import defaultdict 
import argparse
import logging
import os

# Main function to process the input HS text file and generate a JSON schema
def main(paperID, input_hs, output_dir):
    
    # Open the input HS text file and read its content line by line
    with open(os.path.join(input_hs, paperID + '.txt'), 'r') as tex:
        text_con = tex.readlines()
        
    # Initialize dictionaries to store grouped text and event information
    text_dict = defaultdict(list) 
    event_dict = defaultdict(list)

    # Counter for grouping text sections based on empty lines
    cnt = 0
    text_dict['0'] = []

    # Loop through each line of the text file
    for idx, item in enumerate(text_con):
        if item != '\n':  # Non-empty line, add to current group
            text_dict[str(cnt)].append(item)
        else:  # Empty line, start a new group
            cnt += 1
            
    # Process each text group to extract relevant information
    for num in range(len(text_dict)):
        # Extract the number of "sub" occurrences in the first line
        subNUM = text_dict[str(num)][0][0 : -1].lower().count("sub")

        # Extract ID, description, and name from the text group
        ID = text_dict[str(num)][2][10 : -1].lower()
        des = text_dict[str(num)][3][13 : -1]
        name = text_dict[str(num)][1][7 + subNUM * 3 : -1]

        # Determine the "gate" value, or leave it empty if it's 'xxxx'
        if text_dict[str(num)][5][6: -1] != 'xxxx':
            gate = text_dict[str(num)][5][6: -1]
        else:
            gate = ''
        
        # Extract participant information, ignoring 'xxxx' values
        part = text_dict[str(num)][4][14 : -1].split(', ')
        new_part = []   
        if part[0] != 'xxxx':
            for idx in range(len(part)):
                new_part.append(part[idx].split(' ')[-1])
        
        # Extract relations, ignoring 'xxxx' or 'xxx' values
        if text_dict[str(num)][6][11 : -1] != 'xxxx' and text_dict[str(num)][6][11 : -1] != 'xxx':
            relation = text_dict[str(num)][6][11 : -1].split(', ')
        else:
            relation = []
            
        # Store the extracted information in the event dictionary
        # Event name
        event_dict[ID].append(name)
        # Event description
        event_dict[ID].append(des)
        # Event participants
        event_dict[ID].append(new_part)
        # Event relations
        event_dict[ID].append(relation)
        # Event gate
        event_dict[ID].append(gate)

    # Initialize the schema dictionary to build the JSON structure
    schema_dict = {}
    schema_dict['@context'] = []
    schema_dict['sdfVersion'] = "2.2"
    schema_dict['@id'] = paperID
    schema_dict['version'] = "v0"
    schema_dict['events'] = []
    schema_dict['relations'] = []
    schema_dict['entities'] = []

    # Populate the schema dictionary with event information
    for event in event_dict:
        single_event = {}
        single_event['@id'] = event
        single_event['name'] = event_dict[event][0]
        single_event['participants'] = []

        # Add child events if they exist
        if event_dict[event][2] != []:
            single_event['children'] = []
            for even in event_dict[event][2]:
                child_dict = {}
                child_dict['child'] = even.split('_')[0]
                child_dict['importance'] = float(even.split('_')[1][1 : ])
                single_event['children'].append(child_dict)
            single_event['children_gate'] = event_dict[event][4]

        # Additional event metadata
        single_event['wd_node'] = ''
        single_event['wd_label'] = event_dict[event][0]
        single_event['wd_description'] = event_dict[event][1]
        single_event['description'] = event_dict[event][1]
        
        # Add the event to the schema dictionary
        schema_dict['events'].append(single_event)

    # Populate the schema dictionary with relation information
    for event in event_dict:
        if event_dict[event][3] != []:
            for re in range(len(event_dict[event][3])):
                single_relation = {}
                single_relation['@id'] = "Relations/00443/before"
                single_relation['wd_node'] = "wd:Q79030196"
                single_relation['wd_label'] = "before"
                single_relation['wd_description'] = "qualifies something (inception or end of a thing, event, or date) as happening previously to another thing"
                single_relation['relationSubject'] = event_dict[event][3][re].split('>')[0]
                single_relation['relationObject'] = event_dict[event][3][re].split('>')[1]

    # Write the final JSON schema to the output file
    with open(output_dir + paperID + '.json', 'w') as fp:
        json.dump(schema_dict, fp)
        print(paperID + ' finish')

# Function to parse command-line arguments
def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ID", default=None, type=str, required=True)  # ID of the paper to process
    parser.add_argument("--input_dir", default='Schema_Learning/ZeroShot_output/GPT4o_HS', type=str)  # Input directory for HS text files
    parser.add_argument("--output_dir", default='Schema_Learning/ZeroShot_output/Llama3-70B_SDF', type=str)  # Output directory for JSON files
    parser.add_argument("--llm", default='GPT-4o', type=str)  # Optional argument for specifying LLM model name (if applicable)
    args = parser.parse_args()
    return args

# Entry point for the script
if __name__ == "__main__":
    args = _parse_args()
    logging.info("Start")  # Log the start of the process
    main(args.ID, args.input_dir, args.output_dir)  # Call the main function with parsed arguments
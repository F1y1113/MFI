import os
import json

# Define a function to merge contexts
def merge_contexts(*schemas):
    merged_contexts = []
    for schema in schemas:
        for context in schema["@context"]:
            if context not in merged_contexts:
                merged_contexts.append(context)
    return merged_contexts

# Define a function to merge lists and remove duplicates
def merge_lists(list1, list2):
    merged_list = list1.copy()
    for item in list2:
        if item not in merged_list:
            merged_list.append(item)
    return merged_list

# Define a function to merge event details
def merge_event_details(event1, event2):
    merged_event = event1.copy()
    for key in event2:
        if key not in merged_event or not merged_event[key]:
            merged_event[key] = event2[key]
        elif isinstance(event2[key], list):
            merged_event[key] = merge_lists(merged_event[key], event2[key])
        elif isinstance(event2[key], dict):
            merged_event[key] = merge_event_details(merged_event[key], event2[key])
    return merged_event

# Define a function to merge events by name
def merge_events_by_name(*schemas):
    merged_events = {}
    for schema in schemas:
        for event in schema["events"]:
            event_name = event["name"]
            if event_name not in merged_events:
                merged_events[event_name] = event
            else:
                merged_events[event_name] = merge_event_details(merged_events[event_name], event)
    return list(merged_events.values())

# Define a function to merge relations and update event IDs
def merge_relations(*schemas, merged_events):
    merged_relations = []
    name_to_id = {event["name"]: event["@id"] for event in merged_events}
    for schema in schemas:
        for relation in schema["relations"]:
            subject_name = relation["relationSubject"]
            object_name = relation["relationObject"]
            if subject_name in name_to_id and object_name in name_to_id:
                relation["relationSubject"] = name_to_id[subject_name]
                relation["relationObject"] = name_to_id[object_name]
                if relation not in merged_relations:
                    merged_relations.append(relation)
    return merged_relations

# Define a function to merge entities
def merge_entities(*schemas):
    merged_entities = []
    for schema in schemas:
        for entity in schema["entities"]:
            if entity not in merged_entities:
                merged_entities.append(entity)
    return merged_entities

# Main function to merge multiple schemas
def merge_schemas(*schemas):
    merged_schema = {
        "@context": merge_contexts(*schemas),
        "sdfVersion": "2.2",
        "@id": "merged_schema",
        "version": "v0",
        "events": merge_events_by_name(*schemas),
        "relations": [],
        "entities": merge_entities(*schemas)
    }
    merged_schema["relations"] = merge_relations(*schemas, merged_events=merged_schema["events"])
    return merged_schema

# Load all JSON files from a directory
def load_schemas_from_directory(directory):
    schemas = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as f:
                schemas.append(json.load(f))
    return schemas

# Define the directory containing the schema files, change this if needed
# directory = 'ZeroShot_output/Llama3-70B_SDF'
# directory = 'ZeroShot_output/Llama3-3B_SDF'
directory = 'ZeroShot_output/GPT4o_SDF'

# Load schemas from the directory
schemas = load_schemas_from_directory(directory)

# Merge the schemas
merged_schema = merge_schemas(*schemas)

# Save the merged schema to a JSON file
# output_file = "schema_merged/final_schema_ll70b_induction.json"
# output_file = "schema_merged/final_schema_ll3b_induction.json"
output_file = "schema_merged/final_schema_induction.json"
with open(output_file, 'w') as f:
    json.dump(merged_schema, f, indent=2)
    print("success")


print(f"merged schema {output_file} {directory}")

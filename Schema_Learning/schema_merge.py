import json
import os

def load_json_files(directory):
    schemas = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as file:
                schemas.append(json.load(file))
                
    return schemas

def merge_schemas(schemas):
    merged_schema = {
        "@context": schemas[0]["@context"],
        "sdfVersion": schemas[0]["sdfVersion"],
        "@id": "final_schema",
        "version": "v0",
        "events": [],
        "relations": [],
        "entities": [],
        "privateData": {"inputDigest": []},
        "provenanceData": []
    }
    
    event_ids = set()
    
    for schema in schemas:
        for event in schema["events"]:
            if event["@id"] not in event_ids:
                merged_schema["events"].append(event)
                event_ids.add(event["@id"])
        
        for relation in schema.get("relations", []):
            merged_schema["relations"].append(relation)
    
    return merged_schema

def save_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main(directory, output_file):
    schemas = load_json_files(directory)
    merged_schema = merge_schemas(schemas)
    save_json_file(merged_schema, output_file)

if __name__ == "__main__":
    #directory = "modified2"
    directory = "modified2_70"
    #output_file = "final_schemas/final_schema_ll3b_2.json"
    output_file = "final_schemas/final_schema_ll70b_2.json"
    print(f"merged schema {output_file} {directory}")
    main(directory, output_file)

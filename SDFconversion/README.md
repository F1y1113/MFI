# Hierarchical Structure to SDF Conversion

## Overview

```hs2sdf_wgate_3b.py```, ```hs2sdf_wgate_70b.py```, ```hs2sdf_wgate.py```, and ```hs2sdf_wgate.py``` are designed to convert hierarchical structure (HS) text files into Schema Description Format (SDF) JSON files for HS by Llama3-3B, Llama3-70b, and GPT4o. The script reads an input HS text file, processes its content, and generates an SDF-compliant JSON file that represents the extracted events, participants, and relationships.

## Usage

### Command-line arguments
- ```--ID```: (Required) The ID of the paper you want to process. This ID is used to locate the input file and to name the output JSON file.
- ```--input_dir```: The directory containing the input HS text files.
- ```--output_dir```: The directory where the generated JSON files will be saved.

To execute the conversion:
```bash
python hs2sdf_wgat.py --ID <paper_id> --input_dir </path/to/input> --output_dir </path/to/output>
```

## Output
The script generates an SDF-formatted JSON file for each processed HS text file. The JSON file contains:

- Event information (events)
- Participant details (participants)
- Relationships between events (relations)
- 
More detailed information about SDF structure can be found in [SDF](/Schema_Learning/schema_merged/README.md)

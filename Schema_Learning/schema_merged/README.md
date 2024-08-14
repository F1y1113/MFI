# Final Schema SDF

## Overview

Merged from SDF JSON files for each hs text files, the final schema represents the complete lifecycle of EV batteries, from material mining to battery recycling. Each event and subevent is meticulously described and linked, allowing for a clear understanding of the relationships and dependencies within the supply chain.

## Key Components

1. **Context**: The ```@context``` array includes references to the Kairos SDF and CMU context, which provide the necessary structure and standards for interpreting the schema. 
2. **Versioning**: The ```sdfVersion``` specifies the version of the schema format used (2.2).
3. **Events and subevents**: The ```events``` array contains a hierarchical list of all events and subevents related to the EV Battery Supply Chain. Each ```event``` is defined with the following attributes:
    - ```@id```: Unique identifier for the event.
    - ```name```: The name of the event.
    -  ```participants```: Lists the participants involved in the event (currently empty but can be populated if needed).
    - ```children```: Defines subevents and their importance within the parent event.
    - ```children_gate```: Logical gate (“and” or “or”) indicating how the subevents relate to each other.
    - ```wd_node```, ```wd_label```, ```wd_description```: Wikidata references providing additional context about the event.
    - ```description```: A textual description of the event.

4. **Relations**: The ```relations``` array outlines the dependencies and temporal relationships between events using a ```before``` relation, indicating that one event occurs before another. Each relation is described with:
    - ```@id```: A unique identifier for the relation.
    - ```wd_node```, ```wd_label```, ```wd_description```: Wikidata references explaining the type of relation.
    - ```relationSubject```: The event that occurs first.
	- ```relationObject```: The event that occurs afterward.
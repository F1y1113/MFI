# Schema Evaluation Script

## Overview

This script evaluates schema generation against a relation extraction ground-truth dataset. It shall compute evaluation metrics, namely, precision, recall, and F-score, to quantify the quality of the generated schema.

## Features 
**Relation Extraction**: Extracts relations between events from JSON files. 

**Evaluation Metrics**: We compare the instantiated schemas learned by our system with manually annotated ground truth to assess the degree of overlap. For instance, the event of Raw Material Mining includes the subevent of Lithium Mining with an associated importance value, represented by the quadruple subevent(raw material mining, lithium mining, importance). Other relations include participants, gates, sequential events, etc.

To evaluate the results, we 
1. map the events in the learned schema $S_l$ to those in the ground-truth schema Sgt, 
2. establish a one-to-one mapping of quadruples between the learned schema Sl and the ground-truth schema $S_gt$, 
3. calculate Precision, Recall, and F-score as follows:

$$
\text{Precision} = \frac{\text{Number of matched quadruples in } S_l}{\text{Total number of quadruples in } S_l}
$$

$$
\text{Recall} = \frac{\text{Number of matched quadruples in }S_l}{\text{Total number of quadruples in } S_{gt}}
$$

$$
\text{F-score} = 2\cdot \frac{\text{Precision}\cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

## Requirements
- Python 3.8+
- JSON file structured in Schema Definition Files (SDF).

## Usage

1. Prepare directories
    - Directory containing the JSON files of the generated schemas to be evaluated.
    - Directory containing the JSON files of the ground truth schemas.
2. Run the script
```
python evaluate_schema.py <dir_eval> <dir_gt> <output_file>
```

- ```<dir_eval>```: Directory path containing the generated schemas (default: ```sdf_output/```).
- ```<dir_gt>```: Directory path containing the ground truth schemas (default: ```ground_truth/academic/```).
- ```<output_file>```: Path to save the evaluation results in JSON format (default: ```eval/result.json```).
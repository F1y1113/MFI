# SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions

## TOC

<!-- vscode-markdown-toc -->
* 1. [Paper Abstract](#PaperAbstract)
* 2. [Dataset](#Dataset)
	* 2.1. [News Dataset](#NewsDataset)
		* 2.1.1. [Dataset Structure](#DatasetStructure)
		* 2.1.2. [Meta Data](#MetaData)
		* 2.1.3. [Usage](#Usage)
		* 2.1.4. [File Structure](#FileStructure)
* 3. [Schema Learning](#SchemaLearning)
	* 3.1. [Final Merged Schema SDF](#FinalMergedSchemaSDF)
		* 3.1.1. [Key Components](#KeyComponents)
	* 3.2. [Ground Truth Schema](#GroundTruthSchema)
	* 3.3. [Schema Evaluation](#SchemaEvaluation)
		* 3.3.1. [Features](#Features)
		* 3.3.2. [Requirements](#Requirements)
		* 3.3.3. [Usage](#Usage-1)
* 4. [Citation](#Citation)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## Project Links

[Paper](https://arxiv.org/pdf/2408.05357)

[Project Homepage](https://f1y1113.github.io/MFI/)

[Dataset](https://drive.google.com/drive/folders/12kH2S9Rr7ev_XejRZ3HNPhKfk01-dSEv?usp=sharing)



##  1. <a name='PaperAbstract'></a>Paper Abstract

The electric vehicle (EV) battery supply chain's vulnerability to disruptions necessitates advanced predictive analytics. We present SHIELD (Schema-based Hierarchical Induction for EV supply chain Disruption), a system integrating Large Language Models (LLMs) with domain expertise for EV battery supply chain risk assessment. SHIELD combines: (1) LLM-driven schema learning to construct a comprehensive knowledge library,(2) a disruption analysis system utilizing fine-tuned language models for event extraction, multi-dimensional similarity matching for schema matching, and Graph Convolutional Networks (GCNs) with logical constraints for prediction, and (3) an interactive interface for visualizing results and incorporating expert feedback to enhance decision-making. Evaluated on 12,070 paragraphs from 365 sources (2022-2023), SHIELD outperforms baseline GCNs and LLM+prompt method (e.g. GPT-4o) in disruption prediction.These results demonstrate SHIELD's effectiveness in combining LLM capabilities with domain expertise for enhanced supply chain risk assessment.

##  2. <a name='Dataset'></a>Dataset

###  2.1. <a name='NewsDataset'></a>News Dataset

The news dataset contains information related to the EV (Electric Vehicle) battery supply chain, collected for the purpose of testing our schema learning model in the EV battery supply chain prediction project. It is also useful for analyzing and predicting trends in the EV battery supply chain. The dataset encompasses 365 events from January 2022 to December 2023, including international hot news, political events, industrial analysis reports, and news from EV battery companies.

####  2.1.1. <a name='DatasetStructure'></a>Dataset Structure

The dataset is divided into two main parts: `meta_data` and `fused_data`.

####  2.1.2. <a name='MetaData'></a>Meta Data

The `meta_data` consists of independently obtained news events, including details such as titles, dates, content, sources, etc. It is stored in the `./meta_data/` directory.

- `./meta_data/meta_data.xlsx`: This file lists the news articles included in the dataset, detailing their sources, titles, dates, quarters, event types, related countries, and the locations of the corresponding texts.
- `./meta_data/text/`: This folder contains the text of the news articles listed in the metadata.

##### Fused Data

The `fused_data` is created to enhance our model's ability to learn the relationships between events occurring within the same timeframe. It combines hot news, supply chain-related reports, or company news within the same quarter.

- `./fused_data/`: This directory contains the fused data.

####  2.1.3. <a name='Usage'></a>Usage

This dataset can be used for:

- Testing schema learning models for EV battery supply chain prediction.
- Analyzing and predicting trends in the EV battery supply chain.

####  2.1.4. <a name='FileStructure'></a>File Structure

- `./meta_data/`
  - `meta_data.xlsx`: List of recorded news articles with details.
  - `text/`: Folder containing the text of the news articles.
- `./fused_data/`: Folder containing the fused data.

##  3. <a name='SchemaLearning'></a>Schema Learning

###  3.1. <a name='FinalMergedSchemaSDF'></a>Final Merged Schema SDF

Merged from SDF JSON files for each hs text files, the final schema represents the complete lifecycle of EV batteries, from material mining to battery recycling. Each event and subevent is meticulously described and linked, allowing for a clear understanding of the relationships and dependencies within the supply chain.

####  3.1.1. <a name='KeyComponents'></a>Key Components

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

###  3.2. <a name='GroundTruthSchema'></a>Ground Truth Schema

The ground truth schema should specify the EV battery supply chain in its correct and authoritative form. Unlike automatically generated schemas, this ground truth schema is curated by experts who reviewed and validated every single event, relationship, and participant.

###  3.3. <a name='SchemaEvaluation'></a>Schema Evaluation

The ```eval_all.py``` script evaluates schema generation against a relation extraction ground-truth dataset. It shall compute evaluation metrics, namely, precision, recall, and F-score, to quantify the quality of the generated schema.

####  3.3.1. <a name='Features'></a>Features 
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

####  3.3.2. <a name='Requirements'></a>Requirements
- Python 3.8+
- JSON file structured in Schema Definition Files (SDF).

####  3.3.3. <a name='Usage-1'></a>Usage

1. Prepare directories
    - Directory containing the JSON files of the generated schemas to be evaluated.
    - Directory containing the JSON files of the ground truth schemas.
2. Run the script
```
python eval_all.py <dir_eval> <dir_gt> <output_file>
```

- ```<dir_eval>```: Directory path containing the generated schemas (default: ```sdf_output/```).
- ```<dir_gt>```: Directory path containing the ground truth schemas (default: ```ground_truth/academic/```).
- ```<output_file>```: Path to save the evaluation results in JSON format (default: ```eval/result.json```).

##  4. <a name='Citation'></a>Citation

If you found the provided code with our paper useful in your work, please **star** this repo and **cite** our paper!

```
@misc{cheng2024shieldllmdrivenschemainduction,
      title={SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions}, 
      author={Zhi-Qi Cheng and Yifei Dong and Aike Shi and Wei Liu and Yuzhi Hu and Jason O'Connor and Alexander Hauptmann and Kate Whitefoot},
      year={2024},
      eprint={2408.05357},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2408.05357}, 
}
```

# SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions

[![arXiv](https://img.shields.io/badge/arXiv-2408.05357-red)](https://arxiv.org/abs/2408.05357) 
![License](https://img.shields.io/badge/license-MIT-blue) 


**SHIELD** is an advanced framework designed to enhance predictive analytics for the **EV battery supply chain** by integrating **Large Language Models (LLMs)** with domain expertise. The system addresses supply chain vulnerabilities by combining schema learning, event extraction, and predictive modeling, all within an interactive environment for risk assessment.

If you find this repository or our paper useful, please consider **starring** this repository and **citing** our paper:
```bibtex
@inproceedings{cheng2024shield,
  title={SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions},
  author={Cheng, Zhi-Qi and Dong, Yifei and Shi, Aike and Liu, Wei and Hu, Yuzhi and O’Connor, Jason and Hauptmann, Alexander G and Whitefoot, Kate},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
  pages={303--333},
  year={2024}
}
```

## Table of Contents

1. [Overview](#overview)
2. [Dataset](#dataset)
   - [News Dataset](#news-dataset)
     - [Dataset Structure](#dataset-structure)
     - [Meta Data](#meta-data)
     - [Usage](#usage)
     - [File Structure](#file-structure)
3. [Schema Learning](#schema-learning)
   - [Final Merged Schema SDF](#final-merged-schema-sdf)
     - [Key Components](#key-components)
   - [Ground Truth Schema](#ground-truth-schema)
   - [Schema Evaluation](#schema-evaluation)
     - [Features](#features)
     - [Evaluation Metrics](#evaluation-metrics)
     - [Usage](#usage-1)
4. [Citation](#citation)
5. [Contributing](#contributing)
6. [License](#license)

## Overview

The electric vehicle (EV) battery supply chain is highly susceptible to global disruptions, necessitating advanced predictive analytics. We present **SHIELD** (Schema-based Hierarchical Induction for EV Supply Chain Disruption), a system that integrates **Large Language Models (LLMs)** with domain expertise for comprehensive risk assessment of the EV battery supply chain. SHIELD consists of three main components:

1. **LLM-Driven Schema Learning**: Constructs a comprehensive knowledge library by extracting and organizing domain-specific information.
2. **Disruption Analysis System**: Utilizes fine-tuned language models for event extraction, multi-dimensional similarity matching for schema alignment, and Graph Convolutional Networks (GCNs) with logical constraints for predictive modeling.
3. **Interactive Interface**: Provides a user-friendly platform for visualizing results and incorporating expert feedback to refine decision-making processes.

Evaluated on 12,070 paragraphs from 365 sources (2022-2023), SHIELD demonstrates superior performance compared to baseline GCNs and LLM+prompt methods (e.g., GPT-4o) in disruption prediction, showcasing its effectiveness in combining LLM capabilities with domain expertise for enhanced supply chain risk management.

![Project Banner](https://github.com/user-attachments/assets/20a96a6f-b603-4937-b7ff-209f6811242d)

## Dataset

### News Dataset

The news dataset comprises a rich collection of information relevant to the EV (Electric Vehicle) battery supply chain, specifically curated for testing schema learning models and analyzing trends within the EV supply chain context. The dataset spans 365 events from January 2022 to December 2023 and includes:

- International news events
- Political developments
- Industrial analysis reports
- News from EV battery companies

#### Dataset Structure

The dataset is structured into two main components:

1. **Meta Data**: Contains independently obtained news events with details such as titles, dates, content, and sources. This component provides a granular view of individual events.
2. **Fused Data**: Aggregates related news events and reports occurring within the same timeframe to enhance the model's ability to discern relationships between events.

#### Meta Data

Located in the `./meta_data/` directory, the meta data includes:

- `meta_data.xlsx`: A spreadsheet listing all recorded news articles with associated details such as sources, titles, dates, quarters, event types, related countries, and the corresponding text locations.
- `text/`: A folder containing the full text of the news articles referenced in the metadata.

#### Fused Data

The `fused_data` directory contains data that has been combined to strengthen the model's understanding of concurrent events within the same quarter, enabling more robust schema learning and event prediction.

#### Usage

This dataset serves several purposes:

- **Testing schema learning models**: Useful for validating models developed for predicting EV battery supply chain disruptions.
- **Trend analysis and prediction**: Facilitates in-depth analysis of trends and potential disruptions within the EV battery supply chain.

#### File Structure

- **`./meta_data/`**:
  - **`meta_data.xlsx`**: A comprehensive list of news articles with metadata.
  - **`text/`**: Directory containing the news article texts.
- **`./fused_data/`**: Directory containing fused datasets to aid in schema learning.

## Schema Learning

### Final Merged Schema SDF

The **Final Merged Schema SDF** encapsulates the entire lifecycle of EV batteries, from raw material extraction to recycling. This schema meticulously documents every event and sub-event, detailing their relationships and dependencies within the supply chain.

#### Key Components

1. **Context**: The `@context` array includes references to the Kairos SDF and CMU context, which standardize the schema's structure and interpretation.
2. **Versioning**: The `sdfVersion` specifies the schema format version (2.2) to ensure compatibility and consistency.
3. **Events and Sub-events**: The `events` array provides a hierarchical list of all events and sub-events in the EV battery supply chain. Each `event` is defined by:
   - `@id`: A unique identifier.
   - `name`: The event's name.
   - `participants`: Entities involved in the event (can be populated as needed).
   - `children`: Sub-events and their significance within the parent event.
   - `children_gate`: Logical operators (“and” or “or”) defining the relationship between sub-events.
   - `wd_node`, `wd_label`, `wd_description`: Wikidata references for additional context.
   - `description`: A detailed textual description of the event.
4. **Relations**: The `relations` array specifies the dependencies and temporal sequences between events using a `before` relation to indicate precedence.

### Ground Truth Schema

The **Ground Truth Schema** represents the authoritative and expert-validated depiction of the EV battery supply chain. Unlike the automatically generated schemas, this schema is meticulously curated by domain experts to ensure the accuracy and validity of every event, relationship, and participant.

### Schema Evaluation

The `eval_all.py` script evaluates the quality of the generated schema by comparing it to a manually annotated ground truth dataset. It computes key evaluation metrics such as precision, recall, and F-score to quantify the alignment between the generated and ground-truth schemas.

#### Features

- **Relation Extraction**: Extracts relationships between events from JSON files, focusing on understanding event sequences and dependencies.
- **Evaluation Metrics**: We evaluate the overlap between the generated schema and the ground-truth schema. For instance, if the event "Raw Material Mining" includes a sub-event "Lithium Mining" with a specific importance value, this is represented as a quadruple: subevent(raw material mining, lithium mining, importance). Other relationships include participants, logical gates, and sequential dependencies.

#### Evaluation Metrics

To evaluate the results, we:

1. **Map** the events in the learned schema \( S_l \) to those in the ground-truth schema \( S_{gt} \).
2. **Establish** a one-to-one mapping of quadruples between the learned schema \( S_l \) and the ground-truth schema \( S_{gt} \).
3. **Calculate** Precision, Recall, and F-score as follows:

$$
\text{Precision} = \frac{\text{Number of matched quadruples in } S_l}{\text{Total number of quadruples in } S_l}
$$

$$
\text{Recall} = \frac{\text{Number of matched quadruples in } S_l}{\text{Total number of quadruples in } S_{gt}}
$$

$$
\text{F-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

These metrics provide a rigorous assessment of schema alignment, ensuring the learned model's accuracy in representing the ground truth.

#### Usage

1. **Prepare Directories**:
   - Create directories containing the JSON files of both generated schemas (`sdf_output/`) and ground truth schemas (`ground_truth/academic/`).
2. **Run the Evaluation Script**:
   ```bash
   python eval_all.py <dir_eval> <dir_gt> <output_file>
   ```

   - `<dir_eval>`: Path to the directory containing generated schemas.
   - `<dir_gt>`: Path to the directory containing ground truth schemas.
   - `<output_file>`: File path for saving evaluation results in JSON format.

## Citation

If you find this repository or our paper useful, please consider **starring** this repository and **citing** our paper:

```bibtex
@inproceedings{cheng2024shield,
  title={SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions},
  author={Cheng, Zhi-Qi and Dong, Yifei and Shi, Aike and Liu, Wei and Hu, Yuzhi and O’Connor, Jason and Hauptmann, Alexander G and Whitefoot, Kate},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
  pages={303--333},
  year={2024}
}
```

## Contributing

We welcome contributions to this project! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines on how to contribute.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

### Project Links

- [Paper on arXiv](https://arxiv.org/pdf/2408.05357)
- [Project Homepage](https://f1y1113.github.io/MFI/)
- [Download Dataset](https://drive.google.com/drive/folders/12kH2S9Rr7ev_XejRZ3HNPhKfk01-dSEv?usp=sharing)

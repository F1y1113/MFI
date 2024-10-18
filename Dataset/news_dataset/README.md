# EV Battery Supply Chain News Dataset

## Overview

This dataset contains information related to the EV (Electric Vehicle) battery supply chain, collected for the purpose of testing our schema learning model in the EV battery supply chain prediction project. It is also useful for analyzing and predicting trends in the EV battery supply chain. The dataset encompasses 365 events from January 2022 to December 2023, including international hot news, political events, industrial analysis reports, and news from EV battery companies.

The dataset is divided into three main parts: `meta_data`, `fused_data`, and `groundtruth schema`.

## Dataset Structure

### Meta Data

The `meta_data` consists of independently obtained news events, including details such as titles, dates, content, sources, etc. It is stored in the `./meta_data/` directory.

- `./meta_data/meta_data.xlsx`: This file lists the news articles included in the dataset, detailing their sources, titles, dates, quarters, event types, related countries, and the locations of the corresponding texts.
- `./meta_data/text/`: This folder contains the text of the news articles listed in the metadata.

### Fused Data

The `fused_data` is created to enhance our model's ability to learn the relationships between events occurring within the same timeframe. It combines hot news, supply chain-related reports, or company news within the same quarter.

- `./fused_data/`: This directory contains the fused data, which aggregates relevant news articles and reports from similar time periods to form a more comprehensive context for each quarter.

### Groundtruth Schema

The groundtruth schema data is stored in the `./GT_SDF/` directory. This directory contains the schema representation of the news dataset, which serves as the groundtruth for evaluating the schema learning model.

- `./GT_SDF/`: Directory containing the groundtruth schema data for the news dataset.

## Usage

This dataset can be used for:

- Testing schema learning models for EV battery supply chain prediction.
- Analyzing and predicting trends in the EV battery supply chain.
- Evaluating the accuracy of schema learning models using the provided groundtruth schema.

## File Structure

- `./meta_data/`
  - `meta_data.xlsx`: List of recorded news articles with details.
  - `text/`: Folder containing the text of the news articles.
- `./fused_data/`: Folder containing the fused data.
- `./GT_SDF/`: Folder containing the groundtruth schema representation of the news dataset.

## How to Use the Dataset

1. **Schema Learning Model Testing**: The dataset can be used to test schema learning models by comparing the results of the models with the groundtruth schema provided in `./GT_SDF/`.
2. **Trend Analysis**: The `meta_data` and `fused_data` can be used to perform analyses and identify trends in the EV battery supply chain over the period from January 2022 to December 2023.
3. **Relationship Learning**: By utilizing the fused data, users can explore relationships between different events, which may help in predicting future trends or uncovering hidden connections in the EV battery industry.

Feel free to explore the dataset and apply it to your research and analysis tasks. If you encounter any issues or have any questions, please reach out to the dataset maintainers for further assistance.




# EV Battery Supply Chain News Dataset

## Overview

This dataset contains information related to the EV (Electric Vehicle) battery supply chain, collected for the purpose of testing our schema learning model in the EV battery supply chain prediction project. It is also useful for analyzing and predicting trends in the EV battery supply chain. The dataset encompasses 365 events from January 2022 to December 2023, including international hot news, political events, industrial analysis reports, and news from EV battery companies.

## Dataset Structure

The dataset is divided into two main parts: `meta_data` and `fused_data`.

### Meta Data

The `meta_data` consists of independently obtained news events, including details such as titles, dates, content, sources, etc. It is stored in the `./meta_data/` directory.

- `./meta_data/meta_data.xlsx`: This file lists the news articles included in the dataset, detailing their sources, titles, dates, quarters, event types, related countries, and the locations of the corresponding texts.
- `./meta_data/text/`: This folder contains the text of the news articles listed in the metadata.

### Fused Data

The `fused_data` is created to enhance our model's ability to learn the relationships between events occurring within the same timeframe. It combines hot news, supply chain-related reports, or company news within the same quarter.

- `./fused_data/`: This directory contains the fused data.

## Usage

This dataset can be used for:

- Testing schema learning models for EV battery supply chain prediction.
- Analyzing and predicting trends in the EV battery supply chain.

## File Structure

- `./meta_data/`
  - `meta_data.xlsx`: List of recorded news articles with details.
  - `text/`: Folder containing the text of the news articles.
- `./fused_data/`: Folder containing the fused data.



# ANYFILESYNC

## About the Project

ANYFILESYNC is a Python tool that is used to synchronize multi-modal time series data from behavioral (eye tracking, hand movement, etc.) and physiological (ECG,EDA, EMG, etc.) devices into a single CSV file, irrespective of differing sampling rates. This project was inititally developed for a research project that required many different data collection devices. It has since been adapted for general use: for anyone with some basic Python knowledge who wants to combine time series data. 

### How it Works

ANYFILESYNC enforces that the time column in each data modality refers to time in unix seconds. It then combines files using *binning*, where slower recordings are snapped to the nearest time point of faster device recordings. 

## Table of Contents

1. [About the Project](#about-the-project)
2. [Quickstart Guide](#quickstart)
3. [Technical Explanation + Architecture Diagram](#technical-specifications)
4. [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
5. [Usage Guide](#usage-guide)
    * [Data Formatting](#data-formatting)
    * [Code Examples](#code-examples)
6. [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
7. [Required Dependencies](#required-dependencies)
8. [Acknowledgements & Credits](#acknowledgements--credits)

## Quickstart 

First, clone the respository for this project: 

```shell
git clone [this directory]
```

Then, make sure to install all requirements necessary for this project to run 

```shell
pip install -r requirements.txt
```

## Technical Specifications









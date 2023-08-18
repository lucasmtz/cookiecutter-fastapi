# Data Directories

This directory is tracked by dvc, so that the data is versioned and can be shared with other contributors. If you want to ignore some folder or file, you can add it to the `.dvcignore` file.

The data directory is organized as follows:

## external

Data from third party sources

## interim

Datasets created during the interim steps of a data pipeline. This folder is mostly for creating copies of interim datasets for debugging purposes.

## processed

The output datasets from data pipelines. Generally used as the input to modeling.

## raw

The original datasets pulled from a source system.

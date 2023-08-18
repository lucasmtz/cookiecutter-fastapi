# Notebooks are for exploration and communication

Notebook are very effective for exploratory data analysis. However, these tools can be less effective for reproducing an analysis. When we use notebooks in our work, we often subdivide the notebooks folder. For example, notebooks/exploratory contains initial explorations, whereas notebooks/reports is more polished work that can be exported as html to the docs directory.

Since notebooks are challenging objects for source control (e.g., diffs of the json are often not human-readable and merging is near impossible), we recommended not collaborating directly with others on Jupyter notebooks. There are two steps we recommend for using notebooks effectively:

1) Follow a naming convention that shows the owner and the order the analysis was done in. We use the format `<step>-<ghuser>-<description>.ipynb` (e.g., `0.3-bull-visualize-distributions.ipynb`).

2) Refactor the good parts. Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at src/{{cookiecutter.__package_name}}/data/make_dataset.py and load data from data/interim. If it's useful utility code, refactor it to src/{{cookiecutter.__package_name}}.

You can import your code and use it in notebooks with a cell like the following:

```juptyer
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src/{{cookiecutter.__package_name}}, it gets loaded
%autoreload 2

from src.{{cookiecutter.__package_name}}.data import make_dataset
```

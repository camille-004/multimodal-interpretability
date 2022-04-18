# data-science-boilerplate
## Overview
This project assumes you have Anaconda or Miniconda installed on your machine. If you do not, please install from https://docs.conda.io/en/latest/miniconda.html. This is my boilerplate loosely based on [Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science), with modifications including easier Anaconda support, `isort` seeding, pre-commit configs, and Travis CI.

Here's an overview of the directory structure:
- `data`
    - `external` - Data acquired from third-party sources
    - `interim` - Transformed, intermediate data
    - `processed` - Final canonical datasets for modeling
    - `raw` - Original, immutable data dump

- `models` - Trained and serialized models, predictions, or model summaries
- `notebooks` - Exploratory notebooks. Note: According to Cookie Cutter Data Science: "Naming convention is a number (for ordering), the creator's initials, and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`."
- `references` - Data dictionaries, tutorials, explanatory materials
- `reports` - Generalized analysis (i.e., paper), graphics stored in `figures` subdirectory
- `tests` - `pytest` tests
- `src` - Package source code
    - `data` - Scripts to download or generate data
    - `feature_engineering` - Scripts to turn raw data into modeling features
    - `models` - Scripts to train models and generate predictions
    - `visualizations` - Any visualizations to fit your exploratory or business needs

## Getting Started
If you would like to run a CI pipeline, make sure you have an account on [Travis CI](https://www.travis-ci.com/?_gl=1%2A1rbqnop%2A_ga%2ANTAxOTY5NDU3LjE2NTAxODczMDQ.%2A_ga_XRYGSZFQ0P%2AMTY1MDE4NzMwNC4xLjEuMTY1MDE5NzIzMi41OA..) and authorize builds on your GitHub repository. Otherwise, you may remove `.travis.yml`.
1.  `git clone` this repository in the desired directory on your local machine.
2. `cd` into the project directory.
3. To create a conda environment:
    ```
    conda create -n <env_name> dep1 dep2 ...
    conda env export --no-builds --from-history | grep -v "prefix" > environment.yml
    ```
    These in the `export` command flags add only explicit dependencies to `environment.yml` and prevent cross-platform build issues with dependencies during CI. I highly recommend keeping the dependencies in this repository's `environment.yml`.
    If you would like to use the premade `environment.yml` in this project, change the environment name in the file, and create an environment as follows:
    ```
    conda env create -f environment.yml
    ```
4. Run `conda env update && conda activate <env_name>`.
5. Run `pip install -e .`.
6. Run `pre-commit install`.
7. **If you to include test coverage in your build:** In `.travis.yml`, uncomment `python -m pytest tests --cov=src --cov-fail-under=0` and change the `--cov-fail-under` value in  to your intended test coverage percentage.
## Todo; Optional
- Documentation (`docs`) via sphinx or pdoc, requires `README` in RST
- Add a `setup.sh` script to execute the steps above

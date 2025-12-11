# Kaggle - Instant Gratification

This repository contains code, experiments, and analysis for the **Instant Gratification** Kaggle competition.

## Structure

notebooks/       # EDA and experiment notebooks
src/             # All reusable Python modules
experiments/     # YAML experiment configs
data/            # Local data (gitignored)
models/          # Trained model artifacts (gitignored)
output/          # OOF predictions, submissions, logs
submission/      # Final submissions


## How to Run

1. Place Kaggle `train.csv` and `test.csv` into `data/`
2. Start with: `notebooks/01_eda.ipynb`
3. Model training logic is inside `src/models/`
4. Experiment settings inside `experiments/`

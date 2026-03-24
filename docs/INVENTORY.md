# Notebook inventory and classification (classical ML refactor)

This document classifies pre-refactor assets as **keep** (moved into `course/`), **legacy** (archived under `legacy/`), or **new** (added in this refactor).

## Kept and relocated into `course/`

| Original path | Target module | Notes |
| --- | --- | --- |
| `hours_of_studying.ipynb` | `course/01-regression/` | Toy linear regression |
| `california_housing_prediction.ipynb` | `course/01-regression/` | sklearn California housing |
| `hands_on/regression/house-price-prediction-solution.ipynb` | `course/01-regression/` | End-to-end regression |
| `bank_personal_loan.ipynb` | `course/02-classification/` | Multiple classifiers; CSV path normalized |
| `income_classification/income_classification.ipynb` | `course/02-classification/` | Tabular + RandomForest |
| `hands_on/classification/mnist_classification.ipynb` | `course/02-classification/` | Classical workflow on MNIST |
| `hands_on/support_vector_machine/svm.ipynb` | `course/02-classification/` | SVM concepts |
| `solar_flare_svm.ipynb` | `course/02-classification/` | Applied SVM |
| `magic+gamma+telescope/magic_gamma_telescope.ipynb` | `course/02-classification/` | Binary classification |
| `kickstarter_campaign_prediction.ipynb` | `course/06-ensembles-and-boosting/` | Boosting / tabular |
| `p2p_credit_scoring_model_4.ipynb` | `course/02-classification/` | Kept latest P2P iteration |
| `credit-risk-prediction-training-and-eda.ipynb` | `course/04-feature-engineering-and-pipelines/` | Heavy EDA + modeling |
| `indonesia_province_npl_prediction.ipynb` | `course/02-classification/` | Tabular classification |

## Archived to `legacy/` (out of scope, duplicate, or superseded)

| Path | Reason |
| --- | --- |
| `p2p_credit_scoring_model.ipynb`, `p2p_credit_scoring_model_2.ipynb`, `p2p_credit_scoring_model_3.ipynb` | Superseded by `_4` |
| `account_forcasting_regression_model.ipynb` | Overlap with other regression notebooks; typo in name |
| `sklearn_regression/` | Duplicate regression content |
| `pytorch-model-card-classifier.ipynb` | Deep learning (PyTorch) |
| `hands_on/part_2/introduction_to_ann_with_keras/` | Deep learning (Keras) |
| `this_is_jeopardy.ipynb` | EDA exercise, light ML |
| `us-medical-insurance-costs.ipynb` | EDA-focused |
| `energy_consumption.ipynb` | Ambiguous scope; not in core classical path |
| `contruction_cost/` | Typo folder; niche domain |
| `hands_on/regression/house-price-prediction.ipynb` | Superseded by `house-price-prediction-solution.ipynb` |
| `hands_on/regression/house-price-prediction-production-predictor.py` | Optional script; archived with duplicate lesson |
| `.ipynb_checkpoints/` | Jupyter noise (removed from tree; add to `.gitignore`) |
| Root `processed_loans.csv` | Orphan/processed artifact (moved to `legacy/data/` if present) |

## New notebooks added in this refactor

See `SYLLABUS.md` and per-module README files under `course/`.

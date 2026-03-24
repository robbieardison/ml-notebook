# Dataset index

All paths are relative to the repository `data/` directory, resolved at runtime via [utils/data_paths.py](../utils/data_paths.py).

| Dataset / file | Used in | Notes |
| --- | --- | --- |
| `Bank_Personal_Loan_Modelling.csv` | `bank_personal_loan.ipynb` | Tabular classification |
| `kickstarter_data_with_features.csv` | `kickstarter_campaign_prediction.ipynb` | Tabular classification / boosting |
| `p2p_lending_data.csv` | `p2p_credit_scoring_model_4.ipynb` | Credit scoring |
| `income_classification/train.csv`, `test.csv` | `income_classification.ipynb` | Copied under `data/income_classification/` |
| `magic_telescope/magic04.data`, `magic04.names` | `magic_gamma_telescope.ipynb` | UCI MAGIC Gamma Telescope |
| `housing/housing.csv` | `house-price-prediction-solution.ipynb` | Ames-style housing (bundled copy) |
| `transactions.csv` | (legacy / optional) | See `legacy/` if referenced |
| `jeopardy.csv`, `insurance.csv` | Legacy EDA notebooks | Archived under `legacy/` |

## Provenance

- **California housing:** loaded via `sklearn.datasets.fetch_california_housing` (no local CSV).
- **MNIST:** typically fetched via `sklearn.datasets.fetch_openml` in the notebook (check the notebook header).
- **MAGIC:** UCI repository format; column names documented in `magic04.names`.

When adding new datasets, place files under `data/<short_name>/` and document them here.

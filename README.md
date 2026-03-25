# Classical machine learning course (notebooks)

Structured, beginner-to-intermediate **classical ML** material using **scikit-learn** plus optional **statsmodels**, **XGBoost**, and **LightGBM**. Deep-learning notebooks were moved to `legacy/`.

## Quickstart

```bash
cd ml-notebook
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m jupyter lab
```

Open notebooks from `course/` in the order given in [SYLLABUS.md](SYLLABUS.md).

**Important:** Run Jupyter with the **repository root** (`ml-notebook/`) as the working directory so `utils/data_paths.py` can find the `data/` folder. In JupyterLab: *File → Open from Path* or start Lab from this directory.

## Layout

| Path | Purpose |
| --- | --- |
| [course/](course/) | Modules `00`–`09` with teaching notebooks (09 = RL intro) |
| [exercises/](exercises/) | Short exercises per module |
| [data/](data/) | Datasets (see [docs/DATASETS.md](docs/DATASETS.md)) |
| [utils/](utils/) | Shared helpers (`data_dir()` for paths) |
| [docs/](docs/) | Inventory, dataset notes |
| [legacy/](legacy/) | Archived notebooks (duplicates, DL, off-scope) |

## Syllabus

See [SYLLABUS.md](SYLLABUS.md).

## License

See [LICENSE](LICENSE) in the repository.

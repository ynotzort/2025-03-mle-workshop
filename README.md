# 2025-03-mle-workshop

Here we learn the basics of MLE

## How to install UV

- Go to [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- execute the following in the terminal:
 `curl -LsSf https://astral.sh/uv/install.sh | sh`
- now if you run `uv -V` it should output uv ...

## How to use UV to setup day 1

- run inside the folder day_1: `uv init --python 3.10`
- run `uv sync`
- run 
```bash
uv add scikit-learn==1.2.2 pandas pyarrow
uv add --dev jupyter seaborn
```
- after fixing stuff we found out that we also need to run 
`uv add numpy==1.26.4`

if you want to use jupyter notebook, run the following in the terminal:
`uv run jupyter notebook`

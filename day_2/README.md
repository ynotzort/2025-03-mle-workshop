# Day 2

## create the project

`uv init --lib --python 3.10 duration_pred_serve`

add dependencies from day_1:
`uv add scikit-learn==1.2.2 numpy==1.26.4 flask`

copy over model from day 1.

`uv add --dev requests`
`uv add loguru`
`uv add gunicorn`

## Deploy to Cloud (Fly.io)
- create an account at fly.io
- install flyctl: `curl -L https://fly.io/install.sh | sh`
- run:
```
  export FLYCTL_INSTALL="/home/codespace/.fly"
  export PATH="$FLYCTL_INSTALL/bin:$PATH"
```
- copy those lines also to ~/.bashrc

- run `fly launch`

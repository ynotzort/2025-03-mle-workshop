FROM python:3.10-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/0.6.4/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# copy everything from the current folder into the docker image
# ADD . /app/

# copy just the files pyproject.toml uv.lock README.md and the src/ folder over
ADD pyproject.toml uv.lock README.md src/ /app/

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

ADD models/2022-01.pkl model.bin

ENV MODEL_PATH model.bin
ENV VERSION 2022-01-v01
ENV LOGURU_LEVEL INFO

EXPOSE 9696
# ENTRYPOINT [ "bash" ]
# ENTRYPOINT [ "uv", "run", "python", "duration_pred_serve/serve.py" ]
ENTRYPOINT [ \
    "uv", \
    "run", \
    "gunicorn", \
    "--bind=0.0.0.0:9696", \
    "duration_pred_serve.serve:app" \
]

#!/usr/bin/env python
# coding: utf-8

from datetime import date
import pandas as pd

# import seaborn as sns
# import matplotlib.pyplot as plt
import pickle

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline

import logging


logger = logging.getLogger(__name__)


def read_dataframe(filename):
    """
    Loads a parquet file, calculates ride durations, filters by duration (1-60 minutes),
    and converts location IDs to string type.

    Args:
        filename (str): Path to the parquet file.

    Returns:
        pd.DataFrame: Processed DataFrame with ride durations and categorical location IDs.
    """
    logger.info(f"Reading data from {filename}")
    try:
        df = pd.read_parquet(filename)

        df["duration"] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
        df.duration = df.duration.dt.total_seconds() / 60

        df = df[(df.duration >= 1) & (df.duration <= 60)]

        categorical = ["PULocationID", "DOLocationID"]
        df[categorical] = df[categorical].astype(str)

        logger.debug(f"Dataframe shape: {df.shape}")

        return df
    except Exception as e:
        logger.error(f"Something went wrong: {str(e)}")
        raise e


def run(train_date: date, val_date: date, out_path: str):
    logger.info(
        f"Strating a training run for {train_date}, validating on {val_date}. Will save to {out_path}"
    )
    try:
        base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet"

        train_url = base_url.format(year=train_date.year, month=train_date.month)
        val_url = base_url.format(year=val_date.year, month=val_date.month)
        logger.debug(f"{train_url=}")
        logger.debug(f"{val_url=}")

        df_train = read_dataframe(train_url)
        df_val = read_dataframe(val_url)

        logger.debug(f"Length of Training data: {len(df_train)}")
        logger.debug(f"Length of Validation data: {len(df_val)}")

        categorical = ["PULocationID", "DOLocationID"]
        numerical = ["trip_distance"]

        train_dicts = df_train[categorical + numerical].to_dict(orient="records")
        val_dicts = df_val[categorical + numerical].to_dict(orient="records")

        target = "duration"
        y_train = df_train[target].values
        y_val = df_val[target].values

        pipeline = make_pipeline(DictVectorizer(), LinearRegression())
        pipeline.fit(train_dicts, y_train)
        y_pred = pipeline.predict(val_dicts)

        mse = mean_squared_error(y_val, y_pred, squared=False)
        logger.info(f"MSE: {mse}")

        logger.info(f"saving model to {out_path}")
        with open(out_path, "wb") as f_out:
            pickle.dump(pipeline, f_out)
            
        return mse

    except Exception as e:
        logger.error(f"Training failed: {str(e)}")
        raise e


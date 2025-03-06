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


def read_dataframe(filename):
    df = pd.read_parquet(filename)

    df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)
    
    return df


def run(train_date: date, val_date: date, out_path: str):
    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet'

    train_url = base_url.format(year=train_date.year, month=train_date.month)
    val_url = base_url.format(year=val_date.year, month=val_date.month)
    print(f"{train_url=}")
    print(f"{val_url=}")

    df_train = read_dataframe(train_url)
    df_val = read_dataframe(val_url)

    print(f"Length of Training data: {len(df_train)}")
    print(f"Length of Validation data: {len(df_val)}")

    categorical = ['PULocationID', 'DOLocationID']
    numerical = ['trip_distance']

    train_dicts = df_train[categorical + numerical].to_dict(orient='records')
    val_dicts = df_val[categorical + numerical].to_dict(orient='records')

    target = 'duration'
    y_train = df_train[target].values
    y_val = df_val[target].values


    pipeline = make_pipeline(
        DictVectorizer(),
        LinearRegression()
    )
    pipeline.fit(train_dicts, y_train)
    y_pred = pipeline.predict(val_dicts)

    print(f"MSE: {mean_squared_error(y_val, y_pred, squared=False)}")

    print(f"saving model to {out_path}")
    with open(out_path, 'wb') as f_out:
        pickle.dump(pipeline, f_out)

if __name__ == "__main__":
    train_date = date(2022, 1, 1)
    val_date = date(2022, 2, 1)
    run(train_date, val_date, "lin_reg.bin")


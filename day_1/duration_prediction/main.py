from datetime import date
import click
from duration_prediction.train import run
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@click.command(help="Trains the model given a training month and saves it")
@click.option(
    "--train-date", required=True, help="Training Month in the format YYYY-MM"
)
@click.option(
    "--val-date", required=True, help="Validation Month in the format YYYY-MM"
)
@click.option(
    "--model-save-path",
    required=True,
    help="Path where the trained model will be saved",
)
def main(train_date: str, val_date: str, model_save_path: str):
    train_year, train_month = train_date.split("-")
    val_year, val_month = val_date.split("-")
    model_save_path = model_save_path

    train_date = date(int(train_year), int(train_month), 1)
    val_date = date(int(val_year), int(val_month), 1)
    run(train_date, val_date, model_save_path)


if __name__ == "__main__":
    main()

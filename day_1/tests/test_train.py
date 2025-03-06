from datetime import date
from duration_prediction.train import run
import tempfile
from pathlib import Path

def test_train_regression_2022_01():

    with tempfile.TemporaryDirectory() as tmpdirname:
        out_path = Path(tmpdirname) / "model.pkl"
        mse = run(date(2022, 1, 1), date(2022, 2, 1), out_path)
        
        assert abs(mse - 8.1893) < 0.01


def test_train_creates_a_model_file():

    with tempfile.TemporaryDirectory() as tmpdirname:
        out_path = Path(tmpdirname) / "model.pkl"
        assert not out_path.exists()
        _ = run(date(2022, 1, 1), date(2022, 2, 1), out_path)
        assert out_path.exists()
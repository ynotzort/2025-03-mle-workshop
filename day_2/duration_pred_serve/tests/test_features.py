import pytest
from duration_pred_serve.features import prepare_features


def test_prepare_features():
    trip = {
        "PULocationID": 43,
        "DOLocationID": 238,
        "trip_distance": 1.16,
    }

    expected_features = {
        "PULocationID": "43",
        "DOLocationID": "238",
        "trip_distance": 1.16,
    }
    
    result = prepare_features(trip)
    assert result == expected_features

def test_prepare_features_missing_f():
    trip = {
        "PULocationID": 43,
        "trip_distance": 1.16,
    }
    
    with pytest.raises(AssertionError) as e:
        prepare_features(trip)
    assert "Missing Arg: DOLocationID" in str(e.value)

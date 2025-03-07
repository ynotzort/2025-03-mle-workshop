
# "feature engineering"
def prepare_features(ride):
    assert "PULocationID" in ride, "Missing Arg: PULocationID"
    assert "DOLocationID" in ride, "Missing Arg: DOLocationID"
    assert "trip_distance" in ride, "Missing Arg: trip_distance"
    
    features = dict()
    features["PULocationID"] = str(ride["PULocationID"])
    features["DOLocationID"] = str(ride["DOLocationID"])
    features["trip_distance"] = float(ride["trip_distance"])
    return features

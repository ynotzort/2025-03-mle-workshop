import pickle
from pathlib import Path

from flask import Flask, request, jsonify

with Path("./models/2022-01.pkl").open("rb") as f_in:
    model = pickle.load(f_in)
    

# "feature engineering"
def prepare_features(ride):
    assert "PULocationID" in ride
    assert "DOLocationID" in ride
    assert "trip_distance" in ride
    
    features = dict()
    features["PULocationID"] = str(ride["PULocationID"])
    features["DOLocationID"] = str(ride["DOLocationID"])
    features["trip_distance"] = float(ride["trip_distance"])
    return features

def predict(features):
    predictions = model.predict(features)
    return float(predictions[0])

# trip = {
#     "PULocationID": "43",
#     "DOLocationID": "238",
#     "trip_distance": 1.16
# }
# prediction = model.predict(trip)
# print(prediction[0])

app = Flask("duration-prediction")

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    ride = request.get_json()
    features = prepare_features(ride)
    prediction = predict(features)
    result = {
        "prediction": {
            "duration": prediction,
        }
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

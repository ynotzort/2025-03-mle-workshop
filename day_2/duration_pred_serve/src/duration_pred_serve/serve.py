import pickle
from pathlib import Path
import os
from duration_pred_serve.features import prepare_features
from loguru import logger

from flask import Flask, request, jsonify

VERSION = os.getenv("VERSION", "n/a")
MODEL_PATH = os.getenv("MODEL_PATH", "./models/default_model.pkl")

logger.info(f"Starting up Version: {VERSION}")
logger.info(f"Using model: {MODEL_PATH}")
with Path(MODEL_PATH).open("rb") as f_in:
    model = pickle.load(f_in)
    

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
        },
        "version": VERSION
    }
    logger.debug(f"Compute pred for input {features} : {prediction}")
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

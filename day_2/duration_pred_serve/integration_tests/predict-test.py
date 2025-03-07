import requests

# todo steps: 
# - build the docker image
# - start the docker container
# - run this current version of the script
#    - connect to the server
#    - send request and get answer
#    - verify that the answer makes sense
# - stop the docker container

url = "http://127.0.0.1:9696/predict"
trip = {
     "PULocationID": 43,
     "DOLocationID": 238,
     "trip_distance": 1.16
}

response = requests.post(url, json=trip).json()
print(response)

assert "prediction" in response
assert "duration" in response["prediction"]

value = response["prediction"]["duration"]
assert abs(value - 8.434670) < 0.001
print("test passed")
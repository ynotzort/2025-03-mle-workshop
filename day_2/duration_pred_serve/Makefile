VERSION = 2022-01-v01
export VERSION

.PHONY: serve
serve:
	export MODEL_PATH="./models/2022-01.pkl"; \
	uv run python src/duration_pred_serve/serve.py

.PHONY: simple_predict_test
simple_predict_test:
	uv run integration_tests/predict-test.py

docker_build:
	docker build -t duration-prediction .
	
docker_run: docker_build
	docker run -it -p 9696:9696 duration-prediction

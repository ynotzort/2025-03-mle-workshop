
.PHONY: tests
tests: 
	uv run pytest
	
.PHONY: create_model_2022_02
create_model_2022_02: tests
	uv run python -m duration_prediction.main --train-date 2022-01 --val-date 2022-02 --model-save-path models/2022-01.pkl

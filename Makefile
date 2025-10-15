.PHONY: data train

data:
	python -m mlops.dataset --prepare

train:
	python -m mlops.modeling.train

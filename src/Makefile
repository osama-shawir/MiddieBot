install:
	pip install -r requirements.txt

format:	
	black src/*.py api.py

lint:
	pylint --disable=R, api.py src/*py

refactor: format lint
		
all: install lint test format
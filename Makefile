# Build
create-env:
	virtualenv .venv
	source .venv/bin/activate
install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
lint:
	# stop the build if there are Python syntax errors or undefined names
	python -m flake8 . --exclude .venv --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	python -m flake8 . --exclude .venv --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
test:
	python -m pytest -vv --cov-report annotate tests/
format:
	black tests/*.py src/*.py

# Deploy
release:
	semantic-release publish
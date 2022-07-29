compile: install
	pyinstaller --onefile --clean --name move-mouse ./src/main.py

run:
	python ./src/main.py

install:
	pip install -r ./requirements.txt

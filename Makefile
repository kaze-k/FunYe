.PHONY:
	all
	install-all
	install-dev
	install
	compile
	clean
	clear
	lint
	type

.DEAFULT:all

all:
	# install dependencies and compile
	@make compile

install-all:
	# install all dependencies
	@make install
	@make install-dev

install-dev:
	# install develop dependencies
	pip install -e .[dev]

install:
	# install dependencies
	pip install -r ./requirements.txt

compile:install-all
	# compile
	pyinstaller -F ./app.py -n "FunYe" -i ./img/icon.ico

clean:
	# clean up pip cache
	pip cache purge

clear:
	# delete __pycahe__ directory and *.pyc file
	python ./tools/clear.py

lint:
	# lint code
	flake8 src

type:
	# type check
	mypy src

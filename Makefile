# Windows
PY = python

# Linux
# PY = python3

.PHONY:
	all
	venv
	pre-commit
	install-all
	install-dev
	install
	run
	compile
	clean
	clear
	lint
	type
	remove

.DEAFULT:all

all:
	# create venv, install dependencies, compile and pre-commit install
	@make venv
	@make compile
	@make pre-commit

venv:
	# create venv
	$(PY) ./tools/venv.py

pre-commit:
	$(PY) ./tools/devtools.py -p

install-all:
	# install all dependencies
	@make install
	@make install-dev

install-dev:
	# install develop dependencies
	$(PY) ./tools/devtools.py -i dev

install:
	# install dependencies
	$(PY) ./tools/devtools.py -I

run:install
	# run app
	$(PY) ./app.py

compile:install-all
	# compile
	$(PY) ./tools/devtools.py -C

clean:
	# clean up pip cache
	$(PY) ./tools/devtools.py -c

clear:
	# delete __pycahe__ directory and *.pyc file
	$(PY) ./tools/clear.py

lint:
	# lint code
	$(PY) ./tools/devtools.py -l

type:
	# type check
	$(PY) ./tools/devtools.py -t

remove:
	# remove all dependencies(make)
	$(PY) ./tools/devtools.py -r

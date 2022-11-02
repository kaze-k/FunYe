.PHONY:
	all
	venv
	install-all
	install-dev
	install
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
	pre-commit install

venv:
	# create venv
	python ./tools/venv.py

install-all:
	# install all dependencies
	@make install
	@make install-dev

install-dev:
	# install develop dependencies
	python ./tools/devtools.py -i dev

install:
	# install dependencies
	python ./tools/devtools.py -I

compile:install-all
	# compile
	python ./tools/devtools.py -C

clean:
	# clean up pip cache
	python ./tools/devtools.py -c

clear:
	# delete __pycahe__ directory and *.pyc file
	python ./tools/clear.py

lint:
	# lint code
	python ./tools/devtools.py -l

type:
	# type check
	python ./tools/devtools.py -t

remove:
	# remove all dependencies(make)
	python ./tools/devtools.py -r

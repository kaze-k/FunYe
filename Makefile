.PHONY:
	all
	install
	compile
	clean
	clear

.DEAFULT:all

all:
	# install dependencies and compile
	@make compile

install:
	# install dependencies
	pip install -r ./requirements.txt

compile:install
	# compile
	pyinstaller -F ./app.py -n "FunYe" -i ./img/icon.ico

clean:
	# clean up pip cache
	pip cache purge

clear:
	# delete __pycahe__ directory and *.pyc file
	python ./tools/clear.py

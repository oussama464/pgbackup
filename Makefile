.PHONY: install test 

default: test 

install:
	pip install .

test:
	PYTHONPATH=./src pytest
uninstall:
	pip uninstall pgbackup

clean:
	rm -rf ./src/*.egg-info ./build 
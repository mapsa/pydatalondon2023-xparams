.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: myscript


MYRUNS ?= myrun
GLOBALPYTHON ?= python3

all: myscript

myscript:
	@$(GLOBALPYTHON) myrun.py

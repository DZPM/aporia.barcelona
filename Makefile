PELICAN = .venv/bin/pelican
PORT ?= 8002   # not 8000 or 8001: the local server of davidarcos.net uses them

.PHONY: setup build publish serve lint clean

setup:            ## create .venv with the toolchain uv.lock pins (needs uv)
	uv sync --locked

build:            ## build the site into output/ with local settings
	$(PELICAN) content -o output -s pelicanconf.py --fatal errors

publish:          ## build with production settings into output-publish/ (what the workflow runs; fails on warnings), so the local server in output/ keeps working
	$(PELICAN) content -o output-publish -s publishconf.py --fatal warnings

serve: build      ## build and serve at http://127.0.0.1:$(PORT)
	$(PELICAN) --listen -o output -p $(PORT)

lint:             ## check the Python with ruff, and the workflow files with actionlint, if installed (CI runs both)
	.venv/bin/ruff check
	actionlint

clean:
	rm -rf output output-publish

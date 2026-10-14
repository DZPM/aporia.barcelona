PELICAN = .venv/bin/pelican

.PHONY: setup build publish serve lint clean

setup:            ## create .venv with the toolchain uv.lock pins (needs uv)
	uv sync --locked

build:            ## build the site into output/ with local settings
	$(PELICAN) content -o output -s pelicanconf.py --fatal errors

publish:          ## build with production settings (what the workflow runs; fails on warnings)
	$(PELICAN) content -o output -s publishconf.py --fatal warnings

serve: build      ## build and serve at http://127.0.0.1:8000
	$(PELICAN) --listen -o output -p 8000

lint:             ## check the Python with ruff, and the workflow files with actionlint, if installed (CI runs both)
	.venv/bin/ruff check
	actionlint

clean:
	rm -rf output

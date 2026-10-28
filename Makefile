_GREEN:=\033[0;32m
_BLUE:=\033[0;34m
_BOLD:=\033[1m
_NORM:=\033[0m
ENV:=uv run --frozen --
PYTEST_OPTIONS=


.PHONY: help
help:  ## [DEFAULT] Show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?##"}; {printf "${_BLUE}${_BOLD}%-11s${_NORM} %s\n", $$1, $$2}'


.PHONY: all
all:  ## Do everything tagged with [ALL] below
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep "\[ALL\]" | grep -v "^all" | awk 'BEGIN {FS = ":.*?##"}; {printf "%s ", $$1}' | xargs make
	@echo -e "\n    ${_GREEN}${_BOLD}PASS${_NORM}\n"


.PHONY: ruff-format
ruff-format: .venv/.valid ## [ALL] Run 'ruff format'
	${ENV} ruff format


.PHONY: ruff-check
ruff-check: .venv/.valid ## [ALL] Run 'ruff check'
	${ENV} ruff check


.PHONY: test
test: .venv/.valid ## [ALL] Run Unittests via 'pytest' with {PYTEST_OPTIONS}
	${ENV} pytest -vv ${PYTEST_OPTIONS}
	@echo  "See coverage report:\n\n    file://${PWD}/htmlcov/index.html\n"


.PHONY: code
code:  ## Start Visual Studio Code
	code . &


.PHONY: clean
clean:  ## Remove everything mentioned by '.gitignore' file
	git clean -xdf


.PHONY: distclean
distclean:  ## Remove everything mentioned by '.gitignore' file and UNTRACKED files
	git clean -xdf


# Helper
.venv/.valid: pyproject.toml uv.lock
	uv sync --frozen
	@touch $@

uv.lock:
	uv lock
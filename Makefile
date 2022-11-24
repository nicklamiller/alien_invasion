POETRY_RUN := poetry run
LINT_FOLDERS=alien_invasion


autolint:
    @${POETRY_RUN} autopep8 -r -i ${LINT_FOLDERS}
    @${POETRY RUN} unify -r -i ${LINT_FOLDERS}
    @${POETRY_RUN} isort ${LINT_FOLDERS}I

install: install-dev
    poetry install

lint:
    @${POETRY_RUN} flake8 ${LINT_FOLDERS}

precommit: poetry-precommit autolint lint

poetry-precommit:
    poetry run pre-commit run --all-files

shell:
    poetry shell


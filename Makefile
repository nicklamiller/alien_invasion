POETRY_RUN := poetry run
LINT_FOLDERS=alien_invasion

.PHONY: autolint install install-dev lint precommit \
        poetry-precommit shell

autolint:
	@${POETRY_RUN} autopep8 -r -i ${LINT_FOLDERS}
	@${POETRY RUN} unify -r -i ${LINT_FOLDERS}
	@${POETRY_RUN} isort ${LINT_FOLDERS}

install: install-dev
	poetry install

install-dev:
	cp tools/pre-commit .git/hooks
	chmod +x .git/hooks/pre-commit

lint:
	@${POETRY_RUN} flake8 ${LINT_FOLDERS}

precommit: poetry-precommit autolint lint

poetry-precommit:
	poetry run pre-commit run --all-files

shell:
	poetry shell

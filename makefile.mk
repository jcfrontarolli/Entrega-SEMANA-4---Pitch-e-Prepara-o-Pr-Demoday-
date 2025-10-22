.PHONY: dev install run

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r backend/requirements.txt

run:
	. .venv/bin/activate && cd backend && python -m compostech_backend.app

dev: install run
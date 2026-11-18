.PHONY: help check status status-all docker-build docker-up docker-rebuild clean

help:
	@echo "Riseup Help Development Commands:"
	@echo "  make check              - Run site syntax and integrity validator"
	@echo "  make status LANG=es     - Check outdated and missing translations for a language"
	@echo "  make status-all         - Show translation coverage table across all languages"
	@echo "  make docker-build       - Build the Docker image for amber"
	@echo "  make docker-up          - Start amber preview server at http://localhost:8000"
	@echo "  make docker-rebuild     - Completely rebuild static files in public/ using Docker"

check:
	python3 scripts/check_site.py

status:
	@if [ -z "$(LANG)" ]; then \
		echo "Usage: make status LANG=<language_code>"; \
		exit 1; \
	fi
	./what_needs_an_update.sh $(LANG)

status-all:
	./what_needs_an_update.sh --all

docker-build:
	docker compose build

docker-up:
	docker compose up

docker-rebuild:
	docker compose run --rm amber bundle exec amber rebuild

clean:
	rm -rf public/*

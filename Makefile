# Makefile for CloudShop project

PYTHON = python
DB_NAME = cloudNative_hw1.db

.PHONY: init run format clean help

## Initialize the SQLite database
init:
	@echo "🔧 Initializing the database..."
	$(PYTHON) -c "from persistence.database import init_db; init_db()"
	@echo "✅ Database initialized."

## Run the main application
run:
	@echo "🚀 Running CloudShop..."
	$(PYTHON) run.py

## Format code using black
format:
	@echo "🎨 Formatting code with black..."
	black .

## Remove database file
clean:
	@echo "🧹 Removing database file..."
	rm -f $(DB_NAME)
	@echo "🗑️ $(DB_NAME) deleted."

## Show available commands
help:
	@echo "💡 Available commands:"
	@echo "  make init      - Initialize the database"
	@echo "  make run       - Run the main application"
	@echo "  make format    - Format code with black"
	@echo "  make clean     - Delete the SQLite database"
	@echo "  make help      - Show this help message"

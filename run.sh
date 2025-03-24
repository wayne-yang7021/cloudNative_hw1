#!/bin/bash

echo "🔧 Initializing the database..."
python -c "from persistence.database import init_db; init_db()"
echo "✅ Database initialized."

echo "🚀 Running cloudNative_hw1..."
python run.py

#!/bin/bash

# Run script to start the server for testing
# Usage: ./run_server.sh

# Exit immediately if a command exits with a non-zero status
set -e

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run Uvicorn server
echo "Starting Uvicorn server..."
uvicorn API_server:app --host 0.0.0.0 --port 8000 --reload

# Notify the user
echo "Uvicorn server is running. Press Ctrl+C to stop."


#!/bin/bash

# Set up script for environment setup
# Usage: ./setup.sh

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment in the current directory
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip3 install -r requirements.txt
echo "Setup completed. Virtual environment created and dependencies installed."

#pip3 install python-jose
#pip install python-jose

#pip3 install pymongo
#pip install pymongo

pip3 install --upgrade pip



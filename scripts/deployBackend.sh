#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python could not be found. Please install Python 3.9+."
    exit
fi

# Check if virtualenv is installed
if ! pip show virtualenv &> /dev/null
then
    echo "virtualenv is not installed. Installing virtualenv..."
    pip install virtualenv
fi

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

echo "Environment setup complete. Virtual environment created and packages installed."

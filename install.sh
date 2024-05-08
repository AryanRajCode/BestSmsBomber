#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3; then
    echo "Python is not installed. Installing Python..."
    pkg install -y python
    sudo apt update
    sudo apt install -y python3
fi

# Install requests Python module if not installed
if ! python3 -c "import requests" &>/dev/null; then
    echo "Installing requests module..."
    pip install requests
fi

# Run main.py
echo "Running main.py..."
clear
python3 main.py

#!/bin/bash

# Check if Rust is already installed
if ! command -v rustc &> /dev/null; then
    echo "Rust is not installed. Installing Rust..."
    curl https://sh.rustup.rs -sSf | sh -s -- -y
else
    echo "Rust is already installed. Skipping installation."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

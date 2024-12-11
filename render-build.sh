#!/bin/bash
# Install Rust (required for some libraries)
curl https://sh.rustup.rs -sSf | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"

# Install Python dependencies
pip install -r requirements.txt

#!/bin/bash

# Install Python and pip
sudo apt update
sudo apt install python3 python3-pip -y

# Install OpenAI Python API client library
pip3 install openai

# Set up the environment variable for OpenAI API key
echo "export OPENAI_API_KEY='your_openai_api_key_here'" >> ~/.bashrc
source ~/.bashrc

# Install additional LaTeX dependencies
sudo apt install texlive texlive-latex-extra texlive-fonts-recommended -y


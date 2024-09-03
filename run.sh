#!/bin/bash

# Install Python
sudo apt-get update
sudo apt-get install python3 -y

# Init a project
mkdir project
cd project

# Install Flask
pip3 install flask

# Run the Flask application
python3 app.py
#!/usr/bin/env bash

# Update the package list and install necessary packages
apt-get update && apt-get install -y python3 python3-pip python3-dev

# Install required Python packages from the requirements file
pip3 install -r /autograder/source/requirements.txt

# Run the autograder Python script
python3 /autograder/source/autograder.py

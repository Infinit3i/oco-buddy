#!/bin/bash
#
sudo apt update
sudo apt install python3-venv

python3 -m venv oco
source oco/bin/activate
pip install -r requirements.txt


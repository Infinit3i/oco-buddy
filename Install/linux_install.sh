#!/bin/bash

# Update system packages
sudo apt update -y
sudo apt upgrade -y

# Install Python virtual environment tools
sudo apt install python3-venv -y

# Install emoji-compatible fonts
sudo apt install fonts-noto-color-emoji -y

# Set locale to UTF-8 if not already configured
if ! locale | grep -q "UTF-8"; then
  echo "Configuring locale for UTF-8 support..."
  sudo locale-gen en_US.UTF-8
  sudo update-locale LANG=en_US.UTF-8
fi

# Create and activate Python virtual environment
python3 -m venv oco
source oco/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Notify user of completion
echo "Installation complete! Emoji fonts installed and environment ready."

#!/bin/bash
# Update, generate and publish the website with Pelican
echo "Current user: $(whoami)"
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pelican version: $(pelican --version)"
cd ~/GIT/heuzef_com
git pull
make html
make publish
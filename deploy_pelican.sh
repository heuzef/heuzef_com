#!/bin/bash
# Update, generate and publish the website with Pelican
echo "Python version: $(python3 --version)"
echo "Pelican version: $(pelican --version)"
cd ~/GIT/heuzef_com
git pull
make html
make publish
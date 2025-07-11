#!/bin/bash
# Update, generate and publish the website with Pelican
cd ~/GIT/heuzef_com
git pull
make html
make publish
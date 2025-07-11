#!/bin/bash
# Update, generate and publish the website with Pelican
git pull
make html
make publish
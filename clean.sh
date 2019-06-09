#!/bin/bash

chmod 644 .dockerignore .gitignore .travis.yml
chmod 644 LICENSE
chmod 644 README.md
chmod 644 requirements.txt
chmod 644 main.py setup.py

find source test -name "*.json" -exec chmod 644 {} \;
find source test -name "*.py" -exec chmod 644 {} \;
find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.sh" -exec chmod 755 {} \;
find . -name "__pycache__" -exec rm -rf {} \;

#!/bin/bash

pip3 install -U setuptools
pip3 install -U twine
pip3 install -U wheel
pip3 install -Ur requirements.txt

rm -rf buid dist mailtrigger.egg-info/

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*

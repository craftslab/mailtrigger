#!/usr/bin/env bash

pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name mailtrigger --upx-dir /path/to/upx -F trigger.py

#!/bin/bash

pip3 install -U pywin32
pip3 install -U PyInstaller
pip3 install -Ur requirements.txt

pyinstaller --clean --name mailtrigger --upx-dir /path/to/upx -F trigger.py

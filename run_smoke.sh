#!/bin/bash

python3.11 -m pip install -r requirements.txt
python3.11 -m pytest -v -s --headless true -m smoke

exit_code=$?
exit $exit_code
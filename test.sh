#!/usr/bin/env bash
set -e

# E501 line too long
# E701 multiple statements on one line
# Currently, E701 takes issue with some type annotations. (PyCQA/pycodestyle#682)
pycodestyle . --ignore=E501,E701
python3 robot/robot.py test

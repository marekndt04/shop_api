#!/bin/bash

# Run pytest
coverage run -m pytest -rf
flake8
coverage report --fail-under=100
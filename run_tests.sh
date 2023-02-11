#!/bin/bash

# Run pytest
coverage run -m pytest
flake8
coverage report
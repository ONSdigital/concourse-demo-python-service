#!/bin/bash -ex

pipenv install --dev
pipenv run python -m pytest
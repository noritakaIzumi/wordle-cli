#!/usr/bin/env bash

test -d .venv && rm -rf .venv
python -m venv .venv
chmod -R a+x .venv/bin/

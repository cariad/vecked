#!/bin/env bash

set -euo pipefail

cd docs
make doctest

cd ..
pytest -vv

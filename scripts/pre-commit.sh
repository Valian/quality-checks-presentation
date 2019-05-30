#!/usr/bin/env bash

set -e

echo "Running tests..."
cd demo

pytest
flake8

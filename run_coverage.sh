#!/bin/bash
coverage run --source=. classify_triangle_test.py
coverage report -m > results_coverage.txt
coverage html

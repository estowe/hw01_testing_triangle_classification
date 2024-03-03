#!/bin/bash
coverage run --omit '*_test.py' --source=. classify_triangle_test.py 
coverage report -m > results_coverage.txt
coverage html

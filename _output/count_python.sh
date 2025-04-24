#!/bin/bash
# Count the number of lines with the word "python" in all CSV files

count=$(grep -i "python" *.csv | wc -l)
echo "Number of lines containing 'python': $count"

#!/bin/bash

# 1: Make sure folders exist by running setup.sh
./setup.sh

# 2: Stop if the transactions file is missing
if [ ! -f data/transactions.csv ]; then
    echo "ERROR: data/transactions.csv not found. Cannot run nightly job."
    exit 1
fi

# 3: Build a dated report filename
today=$(date +%Y-%m-%d)
report_path="reports/report_${today}.txt"

# 4: Run the Python processing script
python3 src/process.py data/transactions.csv "$report_path"

# 5: Print a short summary
total_lines=$(wc -l < data/transactions.csv)
transaction_count=$((total_lines - 1))

echo ""
echo "=== Nightly Run Summary ==="
echo "Transactions processed from input: $transaction_count"

echo ""
echo "Flagged withdrawals:"
grep "attempted withdrawal" "$report_path" || echo "  None"

# Step 6: Print where the report was saved
echo ""
echo "Full report saved to: $report_path"
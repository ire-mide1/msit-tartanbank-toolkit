#!/bin/bash

# Create required folders if they do not exist
mkdir -p data reports src secrets

echo "Folders created or confirmed: data, reports, src, secrets"

# Check if transactions.csv exists
if [ ! -f data/transactions.csv ]; then
    echo "WARNING: data/transactions.csv not found. Please add it to the data folder."
else
    echo "transactions.csv found in data folder."
fi
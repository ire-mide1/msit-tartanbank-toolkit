#!/bin/bash

# Read the operator id and passphrase from credentials.txt
operator_id=$(grep "operator_id" secrets/credentials.txt | cut -d':' -f2 | tr -d ' ')
passphrase=$(grep "passphrase" secrets/credentials.txt | cut -d':' -f2 | tr -d ' ')

# Compute the SHA-256 hash of the passphrase
hash=$(echo -n "$passphrase" | sha256sum | cut -d' ' -f1)

# Write the operator id and hash (but not the passphrase) to operator.hash
echo "operator_id: $operator_id" > secrets/operator.hash
echo "passphrase_hash: $hash" >> secrets/operator.hash

echo "Stored hashed credentials for operator: $operator_id"
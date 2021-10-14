#!/bin/bash

curl "http://localhost:8000/investments/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "investment": {
      "balance": "'"${BALANCE}"'",
      "description": "'"${DESCRIPTION}"'",
      "risk": "'"${RISK}"'"
    }
  }'

echo

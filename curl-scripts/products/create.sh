#!/bin/bash

curl "http://localhost:8000/products/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "product": {
      "name": "'"${NAME}"'",
      "color": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo

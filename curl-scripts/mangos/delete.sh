#!/bin/bash

curl "http://localhost:8000/products/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo

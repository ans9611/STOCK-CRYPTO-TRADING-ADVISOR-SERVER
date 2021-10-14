#!/bin/bash

curl "http://localhost:8000/products/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo

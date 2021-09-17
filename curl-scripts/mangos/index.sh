#!/bin/bash

curl "http://localhost:8000/products/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo

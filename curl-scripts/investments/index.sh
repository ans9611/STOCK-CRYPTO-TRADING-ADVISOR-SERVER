#!/bin/bash

curl "http://localhost:8000/investments/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo

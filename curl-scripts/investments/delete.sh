#!/bin/bash

curl "http://localhost:8000/investments/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo

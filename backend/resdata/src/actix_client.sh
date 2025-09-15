#!/usr/bin/env bash
# ================================
# Simple Bash client for Actix API
# ================================
# Usage examples:
#   ./actix_client.sh get /health
#   ./actix_client.sh get /users
#   ./actix_client.sh post /users '{"name":"Alice","email":"alice@example.com"}'
#   ./actix_client.sh put /users/1 '{"name":"Bob"}'
#   ./actix_client.sh delete /users/1
#

# BASE_URL="http://localhost:8080"  # Change if your Actix API runs elsewhere
BASE_URL="http://127.0.0.1:8080"
METHOD=$1
ENDPOINT=$2
DATA=$3

if [[ -z "$METHOD" || -z "$ENDPOINT" ]]; then
  echo "Usage: $0 <get|post|put|delete> <endpoint> [json-data]"
  exit 1
fi

# Build curl command
case "$METHOD" in
  get)
    RESPONSE=$(curl -s -X GET "$BASE_URL$ENDPOINT" -H "Accept: application/json")
    ;;
  post)
    RESPONSE=$(curl -s -X POST "$BASE_URL$ENDPOINT" \
      -H "Content-Type: application/json" \
      -d "$DATA")
    ;;
  put)
    RESPONSE=$(curl -s -X PUT "$BASE_URL$ENDPOINT" \
      -H "Content-Type: application/json" \
      -d "$DATA")
    ;;
  delete)
    RESPONSE=$(curl -s -X DELETE "$BASE_URL$ENDPOINT")
    ;;
  *)
    echo "Unsupported method: $METHOD"
    exit 1
    ;;
esac

# Pretty print JSON if jq is installed
echo "$RESPONSE"



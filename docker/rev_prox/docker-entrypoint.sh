#!/bin/bash
set -e
# Start cloudflared in the background
cloudflared tunnel run --token "$CLOUDFLARE_TUNNEL_TOKEN" $CLOUDFLARE_TUNNEL_ID &

# Start nginx in the foreground
nginx -g "daemon off;"

wait # Wait for background processes to complete (optional, depending on your needs)
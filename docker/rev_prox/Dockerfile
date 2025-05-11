FROM nginx:latest

CMD /bin/bash
# Install necessary tools (e.g., curl if needed)
RUN apt-get update && apt-get install -y curl --no-install-recommends

# Install cloudflared (example for Debian/Ubuntu)
ARG CLOUDFLARED_VERSION=latest
RUN mkdir -p --mode=0755 /usr/share/keyrings && \
    curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main" | tee /etc/apt/sources.list.d/cloudflared.list && \
    apt-get update && \
    apt-get install -y cloudflared

# Create a basic cloudflared config (can be minimal or mounted)
RUN mkdir -p /etc/cloudflared
#RUN echo "tunnel: \$CLOUDFLARE_TUNNEL_ID" > /etc/cloudflared/config.yml
#RUN echo "credentials_file: /etc/cloudflared/cert.pem" >> /etc/cloudflared/config.yml

# Set up entrypoint to run both nginx and cloudflared
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

# Your Nginx configuration remains the same
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY default.conf /etc/nginx/conf.d/default.conf
#COPY html /usr/share/nginx/html

EXPOSE 80
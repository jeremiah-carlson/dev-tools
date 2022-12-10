version: '3.8'
services:
  cache:
    image: redis:7.0.5-alpine
    restart: unless-stopped
    ports:
      - '6379:6379'
    command: redis-server --save 100 1 --loglevel warning --requirepass pass
    volumes:
      - cache:/data
    deploy:
      resources:
        limits:
          memory: 2G
volumes:
  cache:
    driver: local
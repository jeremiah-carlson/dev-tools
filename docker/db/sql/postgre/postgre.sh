# !/bin/bash

podman run \
	-v=pg-data:/var/lib/postgresql/data \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_PASSWORD=pg_admin_0123 \
	-p 5432:5432 \
	--name=pg_main \
	--restart=unless-stopped \
	-d docker.io/library/postgres:latest

	

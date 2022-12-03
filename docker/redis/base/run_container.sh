#!/bin/bash

docker network create -d bridge redisnet_base

docker run \
--name redis_base \
--network redisnet_base \
--publish 6379:6379 \
-d redis_base
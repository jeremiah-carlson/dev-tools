#!/bin/bash

docker run \
--name redis_base \
--publish 6379:6379 \
-d redis_base
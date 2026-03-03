import redis
import os
from fastapi import Request, HTTPException

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

MAX_ATTEMPTS = 5
WINDOW_SECONDS = 60

async def rate_limit(request: Request):
    ip = request.client.host
    key = f"login_attempts:{ip}"

    attempts = redis_client.get(key)

    if attempts and int(attempts) >= MAX_ATTEMPTS:
        raise HTTPException(status_code=429, detail="Too many login attempts")

    redis_client.incr(key)
    redis_client.expire(key, WINDOW_SECONDS)
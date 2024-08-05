#!/usr/bin/env python3

import redis
import uuid
from typing import Union
"""
Writing to redis
"""

class Cache:
    """
   Cache class 
    """

    def __init__(self) -> None:
        """Initialize the redis client and flush the db"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data and returns a string"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

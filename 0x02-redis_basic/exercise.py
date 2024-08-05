#!/usr/bin/env python3

import redis
import uuid
from typing import Any, Callable, Optional, Union 
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
    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Gets the key's value and convert it to the needed format"""

        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(value):
            return fn(value)
        return value
    
    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers
        """
        return int(data)

#!/usr/bin/env python3
""" Using Redis in backend """
import redis
import uuid
from functools import wraps
from typing import Callable, Union


class Cache:
    """A class representing a cache system utilizing Redis."""

    def __init__(self):
        """Initialize the Cache instance with a Redis connection."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache and return its unique key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache using the
        provided key and optionally apply a conversion function."""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieve a string data from the cache using the provided key."""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer data from the cache using the provided key."""
        return self.get(key, fn=int)
    def count_calls(method: Callable) -> Callable:
        """Decorator to count the number of times a method is called
        and update the count in the cache."""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache, incrementing the call count, and return its unique key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


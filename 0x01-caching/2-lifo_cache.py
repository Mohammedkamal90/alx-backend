#!/usr/bin/env python3
"""Defines a LIFOCache class that inherits from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system using the LIFO (Last In, First Out) strategy"""

    def __init__(self):
        """Initializes the LIFO cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assigns an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.stack.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()

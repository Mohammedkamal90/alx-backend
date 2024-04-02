#!/usr/bin/env python3
"""define FIFOCache class that inherits from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching system using FIFO (First In, First Out) strategy"""

    def __init__(self):
        """Initializes FIFO cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign an item to cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """retrieve an item from cache"""
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = FIFOCache()
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

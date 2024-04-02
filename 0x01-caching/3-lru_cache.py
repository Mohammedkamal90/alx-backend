#!/usr/bin/env python3
"""Defines a LRUCache class that inherits from BaseCaching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system using the LRU (Least Recently Used) strategy"""

    def __init__(self):
        """Initializes the LRU cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assigns an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue.append(key)

        # Update the queue to reflect the most recently used item
        self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        if key in self.cache_data:
            # Update the queue to reflect the most recently used item
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        else:
            return None


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()

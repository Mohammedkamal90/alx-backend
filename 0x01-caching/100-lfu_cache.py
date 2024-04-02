#!/usr/bin/env python3
"""define LFUCache class that inherits from BaseCaching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """caching system using the LFU (Least Frequently Used) strategy"""

    def __init__(self):
        """Initialize LFU cache"""
        super().__init__()
        self.frequencies = {}

    def put(self, key, item):
        """assign item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key exists, update the item and increase its frequency
            self.cache_data[key] = item
            self.frequencies[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.frequencies[key] = 1

    def get(self, key):
        """retrieve item from cache"""
        if key is None or key not in self.cache_data:
            return None
        self.frequencies[key] += 1
        return self.cache_data[key]

    def evict(self):
        """evict least frequently used item from the cache"""
        min_freq = min(self.frequencies.values())
        least_frequent_keys = [k for k, v in self.frequencies.items() if v == min_freq]
        if len(least_frequent_keys) > 1:
            # If there are multiple least frequently used keys, use any one of them
            least_frequent_key = least_frequent_keys[0]
            del self.cache_data[least_frequent_key]
            del self.frequencies[least_frequent_key]
            print(f"DISCARD: {least_frequent_key}")
        else:
            least_frequent_key = least_frequent_keys[0]
            del self.cache_data[least_frequent_key]
            del self.frequencies[least_frequent_key]
            print(f"DISCARD: {least_frequent_key}")


if __name__ == "__main__":
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()

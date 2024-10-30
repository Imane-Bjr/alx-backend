#!/usr/bin/python3
""" documentation """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """documentation"""

    def __init__(self):
        """documentation"""
        super().__init__()

    def put(self, key, item):
        """documentation"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """documentation"""
        return self.cache_data.get(key)

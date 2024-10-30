#!/usr/bin/python3
""" documentation """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """documentation"""

    def put(self, key, item):
        """documentation"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """documentation"""
        return self.cache_data.get(key)

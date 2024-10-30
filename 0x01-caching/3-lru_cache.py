#!/usr/bin/python3
""" documentation """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """documentaation"""

    def __init__(self):
        """documentation"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """documentation"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """documentation"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)

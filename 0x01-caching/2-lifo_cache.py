#!/usr/bin/env python3
"""
A class LIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class definition."""
    def __init__(self):
        """Initializes a stack."""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                newest_key = self.stack.pop()
                del self.cache_data[newest_key]
                print("DISCARD: {}".format(newest_key))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """Get method."""
        if key is not None:
            return self.cache_data.get(key, None)
        return None

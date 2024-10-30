#!/usr/bin/env python3
"""
A class FIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class definition."""
    def __init__(self):
        """Initializes a queue."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Get method."""
        if key is not None:
            return self.cache_data.get(key, None)
        return None

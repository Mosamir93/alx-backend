#!/usr/bin/env python3
"""
A class BasicCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class definition."""
    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get method."""
        if key is not None:
            return self.cache_data.get(key, None)
        return None

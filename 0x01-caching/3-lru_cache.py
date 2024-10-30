#!/usr/bin/env python3
"""
A class LRUCache that inherits from
BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class definition."""
    def __init__(self):
        """Initializes an ordered dict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                lru_key = self.cache_data.popitem(last=False)[0]
                print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """Get method."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key, None)
        return None

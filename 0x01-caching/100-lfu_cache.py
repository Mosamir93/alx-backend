#!/usr/bin/env python3
"""
A class MRUCache that inherits from
BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class definition."""
    def __init__(self):
        """Initialises a counting dict."""
        super().__init__()
        self.frequency = OrderedDict()

    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS\
                    and key not in self.cache_data:
                lfu_key = min(self.frequency, key=self.frequency.get)
                del self.frequency[lfu_key]
                del self.cache_data[lfu_key]
                print("DISCARD: {}".format(lfu_key))
            if key not in self.frequency:
                self.frequency[key] = 0
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.frequency.move_to_end(key)

    def get(self, key):
        """Get method."""
        if key is not None and key in self.cache_data:
            self.frequency.move_to_end(key)
            self.frequency[key] += 1
            return self.cache_data.get(key)
        return None

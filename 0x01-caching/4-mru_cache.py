#!/usr/bin/env python3
"""
A class MRUCache that inherits from
BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class definition."""
    def __init__(self):
        """"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put method."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS\
                    and key not in self.cache_data:
                mru_key = self.cache_data.popitem()[0]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Get method."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key, None)
        return None

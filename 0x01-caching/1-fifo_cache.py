#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a caching system using the FIFO algorithm
    """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.order = []  # To keep track of the order in which items are added

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the first item put in the cache (FIFO)
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)

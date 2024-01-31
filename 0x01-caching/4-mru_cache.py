#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system using the MRU algorithm
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.insert(0, key)  # Insert at the beginning for MRU

    def get(self, key):
        """ Get an item by key and update its order in the MRU list
        """
        if key in self.cache_data:
            # Move accessed key to the beginning of the order (MRU)
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache_data[key]
        return None

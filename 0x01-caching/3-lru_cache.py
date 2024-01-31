#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a caching system using the LRU algorithm
    """

    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key and update its order in the LRU list
        """
        if key in self.cache_data:
            # Move accessed key to the end of the order (LRU)
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

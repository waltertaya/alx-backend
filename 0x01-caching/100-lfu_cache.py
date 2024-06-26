#!/usr/bin/env python3
""" 100-lfu_cache.py """

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_freq = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.usage_freq[key] += 1
            else:
                self.usage_freq[key] = 1
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_freq = min(self.usage_freq.values())
                least_used_keys = [k for k, v in self.usage_freq.items() if v == least_freq]
                if len(least_used_keys) > 1:
                    discarded_key = next(k for k in self.cache_data if k in least_used_keys)
                else:
                    discarded_key = least_used_keys[0]

                del self.cache_data[discarded_key]
                del self.usage_freq[discarded_key]
                print("DISCARD:", discarded_key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.usage_freq[key] += 1
            return self.cache_data[key]
        return None

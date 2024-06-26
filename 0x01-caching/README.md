# Caching Project

Welcome to the Caching project! This README file will guide you through the different tasks and requirements of this project. The goal is to implement various caching algorithms to understand how they work and their respective use cases.

## Background Context

In this project, you will learn about different caching algorithms. A caching system stores data temporarily to provide faster access to frequently used data and improve performance. Various cache replacement policies manage how data is stored and evicted from the cache.

## Resources

To complete this project, you should read or watch the following resources:

- Cache replacement policies - FIFO
- Cache replacement policies - LIFO
- Cache replacement policies - LRU
- Cache replacement policies - MRU
- Cache replacement policies - LFU

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

- What a caching system is
- What FIFO (First In, First Out) means
- What LIFO (Last In, First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- The purpose of a caching system
- The limits of a caching system

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation
- Documentation should be a real sentence explaining the purpose of the module, class, or method

### BaseCaching Parent Class

All your classes must inherit from the `BaseCaching` class, which is defined below:

```python
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Tasks

### 0. Basic Dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system without any limit.

### 1. FIFO Caching

Create a class `FIFOCache` that inherits from `BaseCaching` and implements a FIFO caching system.

### 2. LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and implements a LIFO caching system.

### 3. LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and implements an LRU caching system.

### 4. MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and implements an MRU caching system.

### 5. LFU Caching

Create a class `LFUCache` that inherits from `BaseCaching` and implements an LFU caching system.

## Repository

- GitHub repository: `alx-backend`
- Directory: `0x01-caching`

## Author

- **@waltertaya**

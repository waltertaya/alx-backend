# 0x00. Pagination

## Description

This project focuses on implementing various pagination techniques in a dataset using Python. You will learn how to paginate data with simple parameters, add hypermedia metadata for pagination, and ensure pagination resilience even when data is deleted between queries.

## Learning Objectives

By the end of this project, you should be able to explain the following without using Google:

- How to paginate a dataset using simple `page` and `page_size` parameters.
- How to paginate a dataset with hypermedia metadata.
- How to paginate in a deletion-resilient manner.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)').
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- All functions and coroutines must be type-annotated.

## Setup

Use the `Popular_Baby_Names.csv` data file for this project.

## Tasks

### Task 0: Simple Helper Function

Write a function named `index_range` that takes two integer arguments, `page` and `page_size`.

- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
- Page numbers are 1-indexed, i.e., the first page is page 1.

**File:** `0-simple_helper_function.py`

### Task 1: Simple Pagination

Copy `index_range` from the previous task and create the following class:

```python
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass
```

Implement the `get_page` method:

- Use `assert` to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset.
- If the input arguments are out of range for the dataset, an empty list should be returned.

**File:** `1-simple_pagination.py`

### Task 2: Hypermedia Pagination

Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:

- `page_size`: the length of the returned dataset page.
- `page`: the current page number.
- `data`: the dataset page (equivalent to return from the previous task).
- `next_page`: number of the next page, None if no next page.
- `prev_page`: number of the previous page, None if no previous page.
- `total_pages`: the total number of pages in the dataset as an integer.

**File:** `2-hypermedia_pagination.py`

### Task 3: Deletion-Resilient Hypermedia Pagination

The goal here is to ensure that if rows are removed from the dataset between two queries, the user does not miss items when changing the page.

Start with the following code:

```python
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        pass
```

Implement the `get_hyper_index` method with two integer arguments: `index` with a None default value and `page_size` with a default value of 10.

The method should return a dictionary with the following key-value pairs:

- `index`: the current start index of the return page.
- `next_index`: the next index to query with.
- `page_size`: the current page size.
- `data`: the actual page of the dataset.

**File:** `3-hypermedia_del_pagination.py`

## Repository

- GitHub repository: `alx-backend`
- Directory: `0x00-pagination`


## Author

- **@waltertaya**

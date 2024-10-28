#!/usr/bin/env python3
"""A simple pagination module."""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the dataset relative to the indices."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """a get_hyper method that takes the same arguments
        as get_page and returns a dictionary"""
        data = self.get_page(page, page_size)
        no_pages = (len(self.dataset()) + page_size - 1) // page_size
        next = page + 1 if page < no_pages else None
        prev = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next,
            "prev_page": prev,
            "total_pages": no_pages
        }


def index_range(page: int, page_size: int) -> Tuple:
    """A function that returns a tuple of a start and an end index."""
    end = page_size * page
    start = (page - 1) * page_size
    return tuple([start, end])

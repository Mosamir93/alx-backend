#!/usr/bin/env python3
"""A function named index_range that takes
two integer arguments page and page_size"""


def index_range(page: int, page_size: int) -> tuple:
    """A function that returns a tuple of a start and an end index."""
    end = page_size * page
    start = (page - 1) * page_size
    return tuple([start, end])

#!/usr/bin/env python3
"""Module to define class Server"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Function to return a tuple of size two containing
       a start index and an end index corresponding to the
       range of indexes to return in a list for those particular
       pagination parameters.
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


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
        """Method that gets the page of the query"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Method that returns a dictionary containing the
           metadata key-value pair"""
        metadata = {}

        start_index, end_index = index_range(page, page_size)
        dataset = self.get_page(page, page_size)

        metadata['page_size'] = len(dataset)
        metadata['page'] = page
        metadata['data'] = dataset

        if len(self.get_page(page + 1, page_size)) > 0:
            metadata['next_page'] = page + 1
        else:
            metadata['next_page'] = None

        metadata['prev_page'] = page - 1 if page > 1 else None

        total_rows = len(self.dataset())
        metadata['total_pages'] = int(math.ceil(total_rows / page_size))

        return metadata

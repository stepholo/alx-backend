#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Method that returns hypermedia pagination metadata based
           on the provided index and page size
        """

        assert index is None or (isinstance(index, int) and 0 <= index <
                                 len(self.dataset())), "Invalid index"

        start_index = index if index is not None else 0
        end_index = start_index + page_size

        dataset_page = self.dataset()[start_index:end_index]

        next_index = end_index if len(dataset_page) > 0 else None

        metadata = {
                'index': start_index,
                'next_index': next_index,
                'page_size': page_size,
                'data': dataset_page
                }

        return metadata

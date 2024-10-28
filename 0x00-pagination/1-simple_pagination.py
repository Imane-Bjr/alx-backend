#!/usr/bin/env python3
""" module documentation """
import csv
import math
from typing import List, Tuple


class Server:
    """Paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ function documentation """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """the cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from our dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """function documentation"""
        startPage = (page - 1) * page_size
        endPage = page * page_size
        return (startPage, endPage)

#!/usr/bin/env python3
"""Pagination function
"""
def index_range(page, page_size):
    """
    return tuple containing start and end index for given page and page size
    Page numbers are 1-indexed
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

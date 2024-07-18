#!/usr/bin/env python3
"""
Task 9
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
    
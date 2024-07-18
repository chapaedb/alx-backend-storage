#!/usr/bin/env python3
"""
Lists all the documents
"""

def list_all(mongo_collection):
    """
    Lists all the doc
    """

    for doc in mongo_collection.find():
                    return doc
    

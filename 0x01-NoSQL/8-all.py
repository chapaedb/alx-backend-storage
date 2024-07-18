#!/usr/bin/ env python3
"""
Lists all the documents
"""

def list_all(mongo_collection):
    """
    Lists all the doc
    """

    if not mongo_collection:
        return []
    else:
            for doc in mongo_collection.find():
                    return doc
    

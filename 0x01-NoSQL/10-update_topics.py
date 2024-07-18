#!/usr/bin/ env python3
"""
Task 10
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates topics based on the name
    """

    mongo_collection.update(
        {'name': name },
        {'$set': {'topics': topics}}
    )

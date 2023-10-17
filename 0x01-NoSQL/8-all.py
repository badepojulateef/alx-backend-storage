#!/usr/bin/env python3
"""
List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    :param mongo_collection: The MongoDB collection to retrieve documents from.
    :type mongo_collection: pymongo.collection.Collection

    :return: A list of all documents in the collection.
    :rtype: list[dict]
    """
    if not mongo_collection:
        return []

    documents = mongo_collection.find()
    return [document for document in documents]

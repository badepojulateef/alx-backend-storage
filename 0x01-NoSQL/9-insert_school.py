#!/usr/bin/env python3
"""
Inserts a new document into a MongoDB collection.
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    :param mongo_collection: The MongoDB collection where the document will be inserted.
    :type mongo_collection: pymongo.collection.Collection

    :param kwargs: Key-value pairs representing the fields and values for the new document.
    :type kwargs: dict

    :return: The ObjectID of the newly inserted document.
    :rtype: pymongo.objectid.ObjectId
    """
    return mongo_collection.insert(kwargs)

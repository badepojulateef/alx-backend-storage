#!/usr/bin/env python3
"""
List of schools having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find schools in a MongoDB collection that have a
    specific topic among their topics.

    :param mongo_collection: The MongoDB collection to search for schools.
    :type mongo_collection: pymongo.collection.Collection

    :param topic: The topic to search for among school topics.
    :type topic: str

    :return: A cursor pointing to the documents that match the specified topic.
    :rtype: pymongo.cursor.Cursor
    """
    return mongo_collection.find({ "topics": topic })

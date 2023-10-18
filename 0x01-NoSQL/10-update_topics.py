#!/usr/bin/env python3
"""
Change all topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics for a school in a MongoDB collection.

    :param mongo_collection: The MongoDB collection where
    the document will be updated.
    :type mongo_collection: pymongo.collection.Collection

    :param name: The name of the school to update.
    :type name: str

    :param topics: The new topics to set for the school.
    :type topics: list

    :return: A pymongo.results.UpdateResult object representing
    the result of the update operation.
    :rtype: pymongo.results.UpdateResult
    """
    return mongo_collection.update_many(
        {
            "name": name
        },
        {
            "$set": {
                "topics": topics
               }
        }
  )

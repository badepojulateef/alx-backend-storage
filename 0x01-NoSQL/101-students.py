#!/usr/bin/env python3
"""
A function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Find and return the top-performing students based
    on their average scores.

    This function uses the MongoDB Aggregation Framework to
    calculate the average score for each student and sorts
    them in descending order by their average score.

    :param mongo_collection: The MongoDB collection containing student data.
    :type mongo_collection: pymongo.collection.Collection

    :return: A cursor pointing to the documents of top-performing students.
    :rtype: pymongo.cursor.Cursor
    """
    pipeline = [
            {
                "$project": {
                    "name": "$name",
                    "averageScore": {
                            "$avg": "$topics.score"
                        }
                }
            },
            {
                "$sort": {
                    "averageScore": -1
                }
            }
     ]

    return mongo_collection.aggregate(pipeleine)

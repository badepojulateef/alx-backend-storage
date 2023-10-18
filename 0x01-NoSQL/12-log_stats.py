#!/usr/bin/env python3
"""
Write a Python script that provides some stats about
Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the
method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this
order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
"""
from pymongo import Mongoclient


def nginx_log_stats(mongo_collection, option=None):
    """
    Provides statistics about Nginx logs stored in a MongoDB collection.

    This function prints the total number of logs and the counts for
    each HTTP method,
    including the number of "GET" requests with the path "/status".

    :param mongo_collection: The MongoDB collection containing Nginx logs.
    :type mongo_collection: pymongo.collection.Collection
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    res = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        nginx_log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_log_stats(mongo_collection)

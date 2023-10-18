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


def nginx_log_stats(mongo_collection):
    """
    Provides statistics about Nginx logs stored in a MongoDB collection.

    This function prints the total number of logs and the counts for
    each HTTP method,
    including the number of "GET" requests with the path "/status".

    :param mongo_collection: The MongoDB collection containing Nginx logs.
    :type mongo_collection: pymongo.collection.Collection
    """
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        counter = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {counter}")

    num_of_gets = mongo_collection.count_documents(
                {"method": "GET", "path": "/status"}
            )
    print(f"{number_of_gets} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_log_stats(mongo_collection)

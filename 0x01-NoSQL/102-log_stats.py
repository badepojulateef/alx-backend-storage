#!/usr/bin/env python3
"""
Improve 12-log_stats.py
"""


def nginx_log_stats2():
    """
    Provides statistics about Nginx logs stored in a MongoDB collection.

    This function calculates and prints various statistics, including the
    total number of logs, the count of each HTTP method, the number of "GET"
    requests with the path "/status", and the top IP addresses by request
    count.

    :return: None
    """
    client = MongoClient()
    collection = client.logs.nginx

    number_of_documents = collection.count_documents({})
    print(f"{number_of_documents} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    print("IPs:")

    pipeline = [
            {
                "$group": {
                    "_id": "$ip",
                    "count": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                     "count": -1
                 }
            },
            {
                "$limit": 10
            },
            {
                "$project": {
                    "_id": 0,
                    "ip": "$_id",
                    "count": 1
                }
            }
    ]

    top_ips = collection.aggregate(pipeline)

    for ip in top_ips:
        count = ip.get("count")
        ip_add = ip.get("ip")
        print("\t{}: {}".format(ip_add, count))


if __name__ == "__main__":
    nginx_log_stats2()

#!/usr/bin/env python3
""" Using pymongo to count clients """
from pymongo import MongoClient


def get_log_stats(mongo_collection):
    """ Returning top 10 ips """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))
    return total_logs, method_stats, status_check_count, top_ips

#!/usr/bin/env python3
""" Provides stats on Nginx stored in MongoDB """


def get_log_stats(mongo_collection):
    """ Getting the stats """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    return total_logs, method_stats, status_check_count

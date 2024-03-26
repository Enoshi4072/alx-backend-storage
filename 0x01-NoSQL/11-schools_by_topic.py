#!/usr/bin/env python3
""" Returns the list of a school with a given topic """


def schools_by_topic(mongo_collection, topic):
    """ Using pipelines """
    pipeline = [
            {"$match": {"topics": topic}}
            ]
    cursor = mongo_collection.aggregate(pipeline)
    schools = list(cursor)
    return schools

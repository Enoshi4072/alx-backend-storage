#!/usr/bin/env python3
""" Sorting in ascednig order based on topics """


def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]

    top_students = list(mongo_collection.aggregate(pipeline))

    return top_students

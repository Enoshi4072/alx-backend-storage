#!/usr/bin/env python3
""" Insert a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Inserting using python """
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id

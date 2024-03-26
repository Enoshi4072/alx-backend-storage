#!/usr/bin/env python3
""" Listing all documents in a collection """
def list_all(mongo_collection):
    """ Using find to get all the documents """
    all_hold = mongo_collection.find()
    documents = []
    for docu in all_hold:
        documents.append(docu)
    return documents

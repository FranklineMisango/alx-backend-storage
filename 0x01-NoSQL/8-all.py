#!/usr/bin/env python3
""" module 8-all """


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    docList = []

    if mongo_collection is None:
        return docList

    for c in mongo_collection.find({}):
        docList.append(c)

    return docList

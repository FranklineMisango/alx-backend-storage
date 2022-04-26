#!/usr/bin/env python3
"""
module: 11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools

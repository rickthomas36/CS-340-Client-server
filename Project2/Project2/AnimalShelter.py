#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:24:09 2024

@author: richardseabri_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """
    CRUD operations for Animal collection in MongoDB
    """

    def __init__(self, user, password):
        USER = 'aacuser'
        PASS = 'Rickthom'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30425
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            if isinstance(data, list):
                insert = self.collection.insert_many(data)
                return insert.inserted_ids  # Returns the list of inserted IDs
            else:
                insert = self.collection.insert_one(data)
                return insert.inserted_id  # Returns the ID of the inserted document
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, search_data=None):
        if search_data:
            data = self.collection.find(search_data, {"_id": False})  # Return a cursor
            return list(data)  # Convert cursor to list
        else:
            data = self.collection.find({}, {"_id": False})  # Return all documents
            return list(data)

    def update(self, filter_data, update_data):
        if filter_data is not None and update_data is not None:
            result = self.collection.update_many(filter_data, {"$set": update_data})
            return result.modified_count  # Returns the number of documents modified
        else:
            raise Exception("Nothing to Update, filter or update data is empty!")

    def delete(self, delete_data):
        if delete_data is not None:
            result = self.collection.delete_many(delete_data)  # Use delete_many if you want to remove multiple
            return result.deleted_count  # Returns the number of documents deleted
        else:
            raise Exception("Nothing to delete, delete data is empty!")


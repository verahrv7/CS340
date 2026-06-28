from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):

        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin'
            % (username, password, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # CREATE
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create Error:", e)
                return False
        else:
            raise Exception(
                "Nothing to save, because data parameter is empty"
            )

    # READ
    def read(self, query):
        if query is not None:
            try:
                data = self.collection.find(query)
                return list(data)
            except Exception as e:
                print("Read Error:", e)
                return []
        else:
            return []
        
            # UPDATE
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print("Update Error:", e)
            return 0

    # DELETE
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete Error:", e)
            return 0
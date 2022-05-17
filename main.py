from datetime import datetime
def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "<yourstring>"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["<dbname>"]
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["<collectioname>"]
    xy = 0
    with open(r"..\fullDB.txt", "r") as dataRead:
        data_base = []
        for line in dataRead:
            data_base.append(line)
        for y in data_base:
            item_1 = {
            "_id" : str(xy),
            "userID" : y
            }
            xy += 1
            collection_name.insert_one(item_1)
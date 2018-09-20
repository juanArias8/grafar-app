from pymongo import MongoClient

# Create mongo client
mongo_client = MongoClient('localhost', 27017)

# Connect to database GrafarDB
grafar_db = mongo_client.GrafarDB

# Connect to graphs document
graphs_2d_collection = grafar_db.graphs2d
graphs_3d_collection = grafar_db.graphs3d

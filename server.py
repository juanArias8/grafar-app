from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
from Graph import Graph
import os

app = Flask(__name__)

# Create mongo client
mongo_client = MongoClient("localhost", 27017)

# Connect to database GrafarDB
grafar_db = mongo_client.GrafarDB

# Connect to graphs document
graphs_collection = grafar_db.graphs


# root
@app.route("/")
def index():
    return "Grafar is a great application!!"


# GET
@app.route("/api")
def get_api():
    data = graphs_collection.find()
    result = ""
    for graph in data:
        string = "<p> Function ==> " + graph["function"] + " </p>" + "<img src=" + graph["image"] + "/>"
        result += string
    return result


# POST
@app.route("/api/data", methods=["POST"])
def get_function():
    json = request.get_json()
    print(json)
    if len(json["function"]) == 0:
        return jsonify({"error": "You should type a function"})
    else:
        function_param = json["function"]

        graph = Graph(function_param)
        image_function = graph.create_graph()
        graphs_collection.insert(
            {"function": function_param, "image": "./static/functions_images/" + image_function + ".png"}
        )
    return jsonify({"Your function is": function_param})


@app.errorhandler(404)
def page_not_found(error):
    return "The place you're looking for does not exist </br> error: %s" % error


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

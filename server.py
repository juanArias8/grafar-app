from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from pymongo import MongoClient
from controllers.controller_graph import Graph
import controllers.controller_database as controller_db

app = Flask(__name__)

# Create mongo client
mongo_client = MongoClient('localhost', 27017)

# Connect to database GrafarDB
grafar_db = mongo_client.GrafarDB

# Connect to graphs document
graphs_collection = grafar_db.graphs

# Define URL folder to save images
url_images = '/home/jnda/PycharmProjects/Grafar/static/functions_images/'


# root
@app.route('/')
def index():
    return 'Grafar is a great application!!'


# GET
@app.route('/api')
def get_api():
    """
    :return: jsonify({"success": boolean, "message": html})
    """

    response_server = ''
    success, message = controller_db.search_all_functions(graphs_collection)
    if success and message is not None:
        data = message
        for graph in data:
            string = '<p> Function ==> ' + graph['function'] + \
                     '</p>' + '<img src=' + graph['image'] + '/>'
            response_server += string
    else:
        response_server = 'There is no functions yet'

    return response_server


# POST
@app.route('/api/data', methods=['POST'])
def get_function():
    """
    :param: data: data is a json {"function": fx, "a": number, "b": number}
    :return: if success:
                return the function image
             if not success:
                json {"message": "Your function is 10*x+2div6","success": true}
    """
    success = False

    json = request.get_json()

    try:
        function_param = json['function']
        a_param = json['a']
        b_param = json['b']
    except Exception as e:
        print(e)
        message = 'You should type a valid function, and the points a and b'
    else:
        graph = Graph(function_param, a_param, b_param, url_images)
        success, function_name = graph.create_graph()
        if success:
            controller_db.insert_graph(graphs_collection, function_name)
            filename = './static/functions_images/' + function_name + '.png'
    if success:
        return send_file(filename, mimetype='image/png')
    else:
        return jsonify({
            "success": success,
            "message": message
        })


@app.errorhandler(404)
def page_not_found(error):
    """
    :param error:
    :return: json{"success": false, "message": error 404 message}
    """
    success = False
    message = str(error)

    return jsonify({
        "success": success,
        "message": message
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

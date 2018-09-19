import os

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import make_response

from flask_restful import Api
from flask_restful import Resource

from resources.client.request import parser_function
from resources.database.database import graphs_collection

from controllers import controller_database
from controllers.controller_graph import Graph2D
from controllers.metadata import FunctionFields

static_folder = './../../static'
template_folder = './../../templates'
kwargs = dict(template_folder=template_folder, static_folder=static_folder)

# Create Flask instance
app = Flask(__name__, **kwargs)

api_client = Api(app)


class Index(Resource):

    def get(self):
        return make_response(render_template('index.html'))


class Function(Resource):

    def post(self):
        success = False
        message = 'Error'
        data_function = parser_function.parse_args()
        try:
            graph = Graph2D(
                data_function[FunctionFields.function],
                data_function[FunctionFields.param_a],
                data_function[FunctionFields.param_b]
            )
            x, y = graph.create_points_graph_2d()
            x, y = str(x), str(y)
            controller_database.insert_graph(
                graphs_collection, data_function[FunctionFields.function], x, y
            )
        except Exception as e:
            print(e)
            message = 'Error ' + str(e)
            success = False
        else:
            message = {'x': x, 'y': y}
            success = True
        finally:
            answer = jsonify({
                'success': success,
                'message': message
            })
        return answer

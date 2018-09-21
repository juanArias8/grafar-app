from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template

from flask_restful import Api
from flask_restful import Resource

from resources.client.request import parser_function
from resources.database.database import graphs_2d_collection
from resources.database.database import graphs_3d_collection

from resources.controllers import controller_database
from resources.utils.metadata import FunctionFields
from resources.controllers.controller_graph import Graph2D
from resources.controllers.controller_graph import Graph3D


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
        type_graph = 0

        data_function = parser_function.parse_args()
        function_str = data_function[FunctionFields.function]
        try:
            if 'y' in function_str:
                x, y, z = self.__convert_function_str_to_graph_3d(data_function)
                self.__save_graph_3d_into_database(
                    graphs_3d_collection, function_str, x, y, z
                )
                message = {'x': x, 'y': y, 'z': z}
                type_graph = 3
            else:
                x, y = self.__convert_function_str_to_graph_2d(data_function)
                self.__save_graph_2d_into_database(
                    graphs_2d_collection, function_str, x, y
                )
                message = {'x': x, 'y': y}
                type_graph = 2
        except Exception as e:
            print(e)
            message = 'Error ' + str(e)
            success = False
        else:
            success = True
        finally:
            answer = jsonify({
                'success': success,
                'message': message,
                'type': type_graph
            })
        return answer

    @staticmethod
    def __convert_function_str_to_graph_3d(data_function):
        graph = Graph3D(
            data_function[FunctionFields.function],
            data_function[FunctionFields.a_value],
            data_function[FunctionFields.b_value]
        )
        x, y, z = graph.create_points_graph_3d()

        return str(x), str(y), str(z)

    @staticmethod
    def __save_graph_3d_into_database(collection, function_str, x, y, z):
        controller_database.insert_3d_graph(
            collection, function_str, x, y, z
        )

    @staticmethod
    def __convert_function_str_to_graph_2d(data_function):
        graph = Graph2D(
            data_function[FunctionFields.function],
            data_function[FunctionFields.a_value],
            data_function[FunctionFields.b_value]
        )
        x, y = graph.create_points_graph_2d()

        return str(x), str(y)

    @staticmethod
    def __save_graph_2d_into_database(collection, function_str, x, y):
        controller_database.insert_2d_graph(
            collection, function_str, x, y
        )

from resources.utils.metadata import FunctionFields
from resources.utils.metadata import Graph2dFields
from resources.utils.metadata import Graph3dFields

"""
controller_database define all operations whit mongodb database
insert, search, update and delete fields from database
"""


def insert_2d_graph(collection, function_str, x, y):
    try:
        collection.insert({
            Graph2dFields.function: function_str,
            Graph2dFields.x: x,
            Graph2dFields.y: y
        })
    except Exception as e:
        print(e)


def insert_3d_graph(collection, function_str, x, y, z):
    try:
        collection.insert({
            Graph3dFields.function: function_str,
            Graph3dFields.x: x,
            Graph3dFields.y: y,
            Graph3dFields.z: z
        })
    except Exception as e:
        print(e)


def search_function(collection, function_str: str) -> tuple:
    success = False
    message = None
    try:
        graph_response = collection.find_one({
            FunctionFields.function: function_str
        })
    except Exception as e:
        print(e)
    else:
        if graph_response is not None:
            success = True
            message = graph_response
    finally:
        return success, message


def search_all_functions(collection) -> tuple:
    success = False
    message = None
    try:
        data = collection.find()
    except Exception as e:
        print(e)
    else:
        if data is not None:
            success = True
            message = data
    finally:
        return success, message

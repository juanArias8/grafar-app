"""
controller_database define all operations whit mongodb database
insert, search, update and delete fields from database
"""


def insert_2d_graph(collection, function_name, x, y):
    try:
        collection.insert({
            'function': function_name,
            'x': x,
            'y': y
        })
    except Exception as e:
        print(e)


def insert_3d_graph(collection, function_name, x, y, z):
    try:
        collection.insert({
            'function': function_name,
            'x': x,
            'y': y,
            'z': z
        })
    except Exception as e:
        print(e)


def search_function(collection, function_name: str) -> tuple:
    success = False
    message = None
    try:
        graph_response = collection.find_one({
            'function': function_name
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

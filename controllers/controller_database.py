"""
controller_database define all operations whit mongodb database
insert, search, update and delete fields from database
"""


def insert_graph(collection, function_name) -> None:
    try:
        url_image = 'static/functions_images/' + function_name + '.png'
        collection.insert({
            'function': function_name,
            'image': url_image
        })
    except Exception as e:
        print("En controller_database.py")
        print(e)


def search_function(collection, function_name: str) -> tuple:
    try:
        success = False
        message = None

        graph_response = collection.find_one({
            'function': function_name
        })

        if graph_response is not None:
            success = True
            message = graph_response

        return success, message
    except Exception as e:
        print(e)


def search_all_functions(collection) -> tuple:
    try:
        success = False
        message = None

        data = collection.find()

        if data is not None:
            success = True
            message = data

        return success, message
    except Exception as e:
        print(e)

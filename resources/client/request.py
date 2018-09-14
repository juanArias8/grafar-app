from flask_restful import reqparse

# Request POST function
parser_function = reqparse.RequestParser(bundle_errors=True)

parser_function.add_argument(
    'function', type=str, required=True, help='function field required'
)
parser_function.add_argument(
    'a', type=int, required=True, help='a field required'
)
parser_function.add_argument(
    'b', type=int, required=True, help='b field required'
)

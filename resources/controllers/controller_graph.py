import sympy as sp
import numpy as np


class Graph2D:
    def __init__(self, function_str, a_value, b_value):
        self.function_str = function_str
        self.a_value = a_value
        self.b_value = b_value

        self.x = sp.Symbol('x')
        self.fx = sp.sympify(self.function_str)

    def __evaluate_fx(self, vector_x, expr):
        f = sp.lambdify(self.x, expr)
        vectorize_f = np.vectorize(f)
        return vectorize_f(vector_x)

    def create_points_graph_2d(self):
        partitions_number = (self.b_value - self.a_value) / 200
        vector_x = np.arange(self.a_value, self.b_value, partitions_number)
        vector_y = self.__evaluate_fx(vector_x, self.fx)

        return vector_x.tolist(), vector_y.tolist()


class Graph3D():
    def __init__(self, function_str, a_value, b_value):
        self.function_str = function_str
        self.a_value = a_value
        self.b_value = b_value

        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.fxy = sp.sympify(self.function_str)

    def __evaluate_fxy(self, vector_x, vector_y, expr):
        f = sp.lambdify((self.x, self.y), expr)
        vectorize_f = np.vectorize(f)
        return vectorize_f(vector_x, vector_y)

    def create_points_graph_3d(self):
        partitions_number = (self.b_value - self.a_value) / 200
        vector_x = vector_y = np.arange(
            self.a_value, self.b_value, partitions_number
        )
        vector_x, vector_y = np.meshgrid(vector_x, vector_y)
        vector_z = self.__evaluate_fxy(vector_x, vector_y, self.fxy)

        return vector_x.tolist(), vector_y.tolist(), vector_z.tolist()


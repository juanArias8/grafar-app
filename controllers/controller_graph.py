import sympy as sym
import numpy as np


# https://plot.ly/javascript/line-charts/
class Graph2D:
    def __init__(self, function_param, a_param, b_param):
        self.function_param = function_param
        self.a_param = a_param
        self.b_param = b_param

        self.x = sym.Symbol('x')
        self.fx = sym.sympify(self.function_param)

    @np.vectorize
    def evaluate_fx(self, x_value):
        return self.fx.subs(self.x, x_value)

    def create_points_graph_2d(self):
        vector_x = np.arange(self.a_param, self.b_param, 0.05)
        vector_y = self.evaluate_fx(self, vector_x)
        return list(vector_x), list(vector_y)


class Graph3D():
    def __init__(self, function_param, a_param, b_param):
        self.function_param = function_param
        self.a_param = a_param
        self.b_param = b_param

        self.x = sym.Symbol('x')
        self.y = sym.Symbol('y')
        self.fxy = sym.sympify(self.function_param)

        def evaluate_fxy(val_x, val_y):
            return float(self.fxy.subs((self.x, val_x), (self.y, val_y)))

        def create_points_graph_3d(self):
            vector_x = vector_y = np.arange(self.a_param, self.b_param, 0.05)
            vector_x, vector_y = np.meshgrid(vector_x, vector_y)

            z = np.array(
                [evaluate_fxy(i, j) for i, j in
                 zip(np.ravel(vector_x), np.ravel(vector_y))]
            )
            z = z.reshape(vector_x.shape)

            return list(vector_x), list(vector_y), list(z)


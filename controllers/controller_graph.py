import sympy as sym
import numpy as np


class Graph:
    def __init__(self, function_param, a_param, b_param):
        self.function_param = function_param
        self.a_param = a_param
        self.b_param = b_param

        self.fx = sym.sympify(self.function_param)
        self.x = sym.Symbol('x')

    @np.vectorize
    def evaluate_fx(self, x_value):
        return self.fx.subs(self.x, x_value)

    def create_graph_points(self):
        x = np.linspace(self.a_param, self.b_param, 1000)
        y = self.evaluate_fx(self, x)

        return list(x), list(y)


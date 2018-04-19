import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, function_param, images_path):
        self.function_param = function_param
        self.fx = sym.sympify(self.function_param)
        self.x = sym.Symbol("x")
        self.images_path = images_path

    @np.vectorize
    def evaluate_fx(self, x_value):
        return self.fx.subs(self.x, x_value)

    def create_graph(self):
        vector = np.linspace(-np.pi, np.pi, 1000)
        fx_evaluated = self.evaluate_fx(self, vector)
        figure = plt.figure()
        plt.plot(vector, fx_evaluated, "-r", label="function f(x) = %s" % self.function_param)
        plt.show()
        figure.savefig(self.images_path + str(self.function_param) + '.png')
        return self.function_param

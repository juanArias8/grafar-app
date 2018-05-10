import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, function_param, a_param, b_param, ulr_images):
        self.function_param = function_param
        self.a_param = a_param
        self.b_param = b_param

        self.url_images = ulr_images

        self.fx = sym.sympify(self.function_param)
        self.x = sym.Symbol("x")

    @np.vectorize
    def evaluate_fx(self, x_value):
        return self.fx.subs(self.x, x_value)

    def create_graph(self):
        success = False
        function_name = None

        vector = np.linspace(self.a_param, self.b_param, 1000)
        fx_evaluated = self.evaluate_fx(self, vector)

        try:
            figure = plt.figure()
            plt.plot(vector, fx_evaluated)
            plt.show()
            function_name = self.__replace_div_in_function(self.function_param)
            self.__save_figure_in_folder(figure, self.url_images, function_name)

            success = True
        except Exception as e:
            print(e)

        return success, function_name

    @staticmethod
    def __replace_div_in_function(function_name: str) -> str:
        function_name = function_name.replace("/", "div")
        return function_name

    @staticmethod
    def __replace_div_out_function(function_name: str) -> str:
        function_name = function_name.replace("div", "/")
        return function_name

    @staticmethod
    def __save_figure_in_folder(figure, url_images: str, function_name: str)\
            -> None:
        figure.savefig(url_images + function_name + ".png")

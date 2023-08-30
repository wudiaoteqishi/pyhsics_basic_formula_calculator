import math

import sympy as sp


class Constants(object):
    def symbol(self):
        self.e = sp.E#自然常数
        self.pi = sp.pi#圆周率
        self.g = 9.8#重力加速度
        self.G = 6.67408e-11#万有引力常数

    def value(self):
        self.e = math.e#自然常数
        self.pi = math.pi#圆周率
        self.g = 9.8#重力加速度
        self.G = 6.67408e-11#万有引力常数

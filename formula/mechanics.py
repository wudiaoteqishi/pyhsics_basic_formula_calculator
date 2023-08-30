import math

from constants.constants import Constants


class Mechanics(Constants, object):
    def __init__(self, representation="symbol"):
        if representation == "symbol":
            super().symbol()
        elif representation == "value":
            super().value()

    @staticmethod
    def work(force=None, distance=None, work=None, angle=0):
        """计算功，角度用弧度制"""
        if work is None and force is not None and distance is not None:
            if angle % (math.pi / 2) == 0:
                return 0
            else:
                return force * distance * math.cos(angle)
        elif force is None and work is not None and distance is not None:
            return work / distance / math.cos(angle)
        elif distance is None and work is not None and force is not None:
            return work / force / math.cos(angle)
        else:
            return "error"

    @staticmethod
    def newtown2th(mass=None, acceleration=None, force=None):
        """计算牛顿第二定律"""
        if force is None and mass is not None and acceleration is not None:
            return mass * acceleration
        elif mass is None and force is not None and acceleration is not None:
            return force / acceleration
        elif acceleration is None and force is not None and mass is not None:
            return force / mass
        else:
            return "error"

    @staticmethod
    def power(work=None, time=None, force=None, speed=None):
        """计算功率"""
        if work is None and time is None and force is not None and speed is not None:
            return force * speed
        elif force is None and speed is None and work is not None and time is not None:
            return work / time
        else:
            return "error"

    @staticmethod
    def energy(mass=None, speed=None, energy=None):
        """计算动能"""
        if energy is None and mass is not None and speed is not None:
            return mass * speed ** 2 / 2
        elif mass is None and speed is not None and energy is not None:
            return 2 * energy / speed ** 2
        elif speed is None and energy is not None and mass is not None:
            return math.sqrt(2 * energy / mass)
        else:
            return "error"

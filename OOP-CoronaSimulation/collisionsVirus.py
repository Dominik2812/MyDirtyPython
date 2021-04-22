import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation
from itertools import count



class Virus:


    def __init__(self, x, y, vx, vy, radius):

        self.r = np.array((x, y))
        self.v = np.array((vx, vy))
        self.radius = radius

        self.styles = {'edgecolor': 'r', 'fill': False}
        self.lifeticker=count()
        self.lifetime=0


    @property
    def x(self):
        return self.r[0]
    @x.setter
    def x(self, value):
        self.r[0] = value
    @property
    def y(self):
        return self.r[1]
    @y.setter
    def y(self, value):
        self.r[1] = value
    @property
    def vx(self):
        return self.v[0]
    @vx.setter
    def vx(self, value):
        self.v[0] = value
    @property
    def vy(self):
        return self.v[1]
    @vy.setter
    def vy(self, value):
        self.v[1] = value


    def overlaps(self, other):
        return np.hypot(*(self.r - other.r)) < self.radius + other.radius

    def draw(self, ax):
        print('draw Virus')

        circle = Circle(xy=self.r, radius=self.radius, **self.styles)
        ax.add_patch(circle)
        return circle

    def advance(self, dt):
        self.r += self.v * dt
        self.lifetime+=1 
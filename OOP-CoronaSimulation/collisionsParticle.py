import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation
from itertools import combinations



class Particle:
    """A class representing a two-dimensional particle."""

    def __init__(self, x, y, vx, vy, radius, virus=None,  styles=None):
        """Initialize the particle's position, velocity, and radius.

        Any key-value pairs passed in the styles dictionary will be passed
        as arguments to Matplotlib's Circle patch constructor.

        """

        self.r = np.array((x, y))
        self.v = np.array((vx, vy))
        self.radius = radius
        self.Container=virus
        
        # if virus:
        if len(self.Container)>0:
            print(len(self.Container))

            self.virus = virus[0]
            virus[0].radius = 0.1*self.radius
            virus[0].x = self.x-virus[0].radius 
            virus[0].y = self.y -virus[0].radius 
            # self.vx = virus.vx
            # self.vy = virus.vy


        

        self.styles = styles
        if not self.styles:
            # Default circle styles
            self.styles = {'edgecolor': 'b', 'fill': False, 'label': True}

    # For convenience, map the components of the particle's position and
    # velocity vector onto the attributes x, y, vx and vy.
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
        """Does the circle of this Particle overlap that of other?"""
        return np.hypot(*(self.r - other.r)) < self.radius + other.radius

    def draw(self, ax):
        """Add this Particle's Circle patch to the Matplotlib Axes ax."""
        print('draw Particle')
        circle = Circle(xy=self.r, radius=self.radius, **self.styles)
        # circle.label='hello'
        # ax.text='hello'

        ax.add_patch(circle)
        
        
        return circle

    def advance(self, dt):
        """Advance the Particle's position forward in time by dt."""
        # if self.virus:
        #     self.r += self.virus.v * dt

        self.r += self.v * dt
        # print('Particle=',self.r)
        # print('Virus=',self.virus.r)
        if len(self.Container)>0:
            self.Container[0].v = self.v 
        # print('Virus nach anpassung=',self.virus.r)
        # ax.annotate("cpicpi", xy=(self.x, self.y), fontsize=3)
        # self.virus.r += self.virus.v * dt

        # Make the Particles bounce off the walls
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx
            # self.styles = {'edgecolor': 'y', 'fill': True}
            # print("left")
        if self.x + self.radius > 1:
            self.x = 1-self.radius
            self.vx = -self.vx
            # self.styles = {'edgecolor': 'y', 'fill': 'r'}
            # print('right')
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy
            # self.styles = {'edgecolor': 'y', 'fill': 'r'}
            # print('top')
        if self.y + self.radius > 1:
            self.y = 1-self.radius
            self.vy = -self.vy
            # self.styles = {'edgecolor': 'y', 'fill': 'r'}
            # print('bottom')


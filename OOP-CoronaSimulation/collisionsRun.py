import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation
from itertools import combinations
from collisionsParticle import Particle
from collisionsSimulation import Simulation




if __name__ == '__main__':
    nparticles = 30
    radii = np.random.random(nparticles)*0.01+0.04
    sim = Simulation(nparticles, radii)
    sim.do_animation(save=False)

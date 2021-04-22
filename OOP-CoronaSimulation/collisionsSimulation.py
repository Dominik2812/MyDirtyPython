from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation
from itertools import combinations
from collisionsParticle import Particle
from collisionsVirus import Virus
import random
from itertools import count

from functools import lru_cache




class Simulation:
    

    def __init__(self, n, radius, styles=None):

        self.init_particles(n, radius, styles)

    def init_particles(self, n, radius, styles=None):
        self.n = n
        self.particles = []
        self.viruses = []


#####################################define particle parameters and create them
        for _, rad in enumerate(radius):

            while True: 
                x, y = rad + (1 - 2*rad) * np.random.random(2)
                vr = 0.05 * np.random.random() + 0.05
                vphi = 2*np.pi * np.random.random()
                vx, vy = vr * np.cos(vphi), vr * np.sin(vphi)
                Container=list()
                vr = 0.05 * np.random.random() + 0.05
                vphi = 2*np.pi * np.random.random()
                vx, vy = vr * np.cos(vphi), vr * np.sin(vphi)
                particle = Particle(x, y, vx, vy, rad ,Container)
                for p2 in self.particles:
                    if p2.overlaps(particle):
                        break
                else:
                    self.particles.append(particle)
                    break


#####################################infect some of the particles
        self.infectedParticles=[]
        for i in range(10):

            infectedParticleIndex=random.randint(0, len(self.particles)-1)
            while self.particles[infectedParticleIndex] in self.infectedParticles:
                infectedParticleIndex=random.randint(0, len(self.particles)-1)


            v_vir=self.particles[infectedParticleIndex].v
            r_vir=self.particles[infectedParticleIndex].r
            radius_vir=self.particles[infectedParticleIndex].radius *0.1

            virus=Virus(r_vir[0] + radius_vir, r_vir[1]+radius_vir, v_vir[0], v_vir[1], radius_vir)
            
            self.particles[infectedParticleIndex].Container.append(virus)
            self.viruses.append(virus)
            self.infectedParticles.append(self.particles[infectedParticleIndex])

            


    def handle_collisions(self):
        print('handle_collisions')

        def transmitVirus(p1, p2):
            if len(p2.Container) >0 or len(p1.Container) >0:
                if len(p2.Container) > len(p1.Container):
                    trans=p2.Container[0] #.pop(0)

                    v_vir=p1.v
                    r_vir=p1.r
                    radius_vir=trans.radius

                    newVirus=Virus(r_vir[0] + radius_vir, r_vir[1]+radius_vir, v_vir[0], v_vir[1], radius_vir)
                    p1.Container.append(newVirus)
                    newVirus.x=p1.x + trans.radius
                    newVirus.y=p1.y + trans.radius
                    self.viruses.append(newVirus)
                    self.virCircles.append(newVirus.draw(self.ax))

                    
                elif len(p2.Container) < len(p1.Container):
                    trans=p1.Container[0] #.pop(0)
                    v_vir=p2.v
                    r_vir=p2.r
                    radius_vir=trans.radius

                    newVirus=Virus(r_vir[0] + radius_vir, r_vir[1]+radius_vir, v_vir[0], v_vir[1], radius_vir)
                    p2.Container.append(newVirus)
                    newVirus.x=p2.x + trans.radius
                    newVirus.y=p2.y + trans.radius
                    self.viruses.append(newVirus)
                    self.virCircles.append(newVirus.draw(self.ax))     
#####################################transmit virus between particles that are too close
        pairs = combinations(range(self.n), 2)
        for i,j in pairs:
            if self.particles[i].overlaps(self.particles[j]):
                transmitVirus(self.particles[i], self.particles[j])
##################################### draw all particles and viruses 
    def initAnimation(self):
        """Initialize the Matplotlib animation."""
        print('initAnmination')
        self.circles = []
        self.virCircles = []
        for particle in self.particles:
            self.circles.append(particle.draw(self.ax))
        for virus in self.viruses:
            self.virCircles.append(virus.draw(self.ax))
        return self.circles, self.virCircles

##################################### move all particvles and viruses
#####################################
#####################################
    def advance_animation(self, dt):
        print('advanceAnimation')
        ##################################### check if existing viruses are drawn
        if len(self.virCircles)< len(self.viruses):
            dif = len(self.viruses) - len(self.virCircles)
            for i in range(1,dif):
                print('draw missing virus')
                self.virCircles.append(self.viruses[-i].draw(self.ax))
        ##################################### move viruses
        if len(self.viruses)>0:
            for i, v in enumerate(self.viruses):
                v.advance(dt)
                ##################################### set them to rest if viruses exceeded lifetime
                if v.lifetime >20: 
                    v.x=0
                    v.y=0 
                self.virCircles[i].center = v.r


        ##################################### move particles
        #####################################
        for i, p in enumerate(self.particles):
            p.advance(dt)
            ##################################### remove viruses from their container that exceeeded their lifetime
            if len(p.Container)>0 and p.Container[0].lifetime>20:
                trans=p.Container.pop(0)
                 ##################################### delete those viruses and from the virusses and virCirclesList
                if trans in self.viruses:
                    index= self.viruses.index(trans)
                    self.viruses.pop(index)
                    self.virCircles.pop(index)
            self.circles[i].center = p.r
        self.handle_collisions()
        return self.circles, self.virCircles


#####################################The function passed to Matplotlib's FuncAnimation routine.
    def animate(self, i):
        print('animate')
        self.advance_animation(0.05)
        return self.circles, self.virCircles


    def do_animation(self, save=False):
        print('doAnimation')




        

        #####################################simulation
        fig, self.ax = plt.subplots()
        print(self.ax)
        for s in ['top','bottom','left','right']:
            self.ax.spines[s].set_linewidth(2)
        self.ax.set_aspect('equal', 'box')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.xaxis.set_ticks([])
        self.ax.yaxis.set_ticks([])
        ##################################### plot the graph
        fig2=plt.figure()
        ax=fig2.add_subplot(1,1,1)
        x_vals=[]
        y_vals=[]
        index=count()
        print(index)
        
        def runAnimation(i):
            x_vals.append(next(index))
            y_vals.append(len(self.viruses))
            ax.cla()   

            if next(index)==10:
                self.ax.cla()
            line=ax.plot(x_vals,y_vals)

        

        anim = [animation.FuncAnimation(fig, self.animate, init_func=self.initAnimation, interval=50),animation.FuncAnimation(fig2, runAnimation,  interval=50)]
           
        plt.show()




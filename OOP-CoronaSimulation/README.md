# OOP Corona Simulation in Python

## Description
A simple and object orientated approach to simulate the dynamics of a pandemic. The code is based on the collisions simulation (https://scipython.com/blog/two-dimensional-collisions/). A population of circles is trapped in a field (such as people are in office) and move randomly and bounce of the borders. A certain percentage of the circles (blue) contain a virus (red ). Circles that overlap eachother transmit a copy of their virus if the opponent is virus free. 

![Simulation](Simulation.png?raw=true "Simulation")

However each virus has a certain lifetime after which it disappears. The number of viruses in the field is plotted in time

![Plot](Plot.png?raw=true "Plot")

Whether the pandemic ceases or increases depends on the circle radia, number of circles and the life time of the viruses.
Enjoy playing around with these parameters ;)

## How to use it
Save all files in the same directory and run Run.py
Also, the number of circles can be tuned in Run.py

The life time of the viruses can be tuned in Simulation.py def advance_animation


## yet to be done
The code here is a base for further development. Such as speeding up the simulation by replacing for loops with quicksearch meachanisms, Mobility patterns: let the circles go to work,restaurants and stay at home, Superspreader events and infectivity by tuning the probability of transmission.
...
Whenever I will find the time I'll dedicate myself to these developments
Any suggestions and solutions are highly welcome. 



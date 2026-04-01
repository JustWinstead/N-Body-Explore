import numpy as np
import math
G = 6.6743e-11 # Grav constant: 6.6743 x 10^(-11) m^3/(kg * s^2)

# Body object to be used in equations
class Body:
    def __init__(self, name, mass, pos, velo, accel):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.velo = velo
        self.accel = accel

# Newtonian accleration
#   system is a list (or some other data structure) of body objects   
#   i is the specific object we want to get the acceleration of
def newtAcceleration(system, i):
    accel = np.zeros(3) # Array to represent acceleration vector
    for j in system:
        if j == i:
            continue # Guard to prevent divide by zero (if qi = qj, then diff = 0)
        # defining placeholder variables is for cowards
        accel += ( G * j.mass * (j.pos - i.pos) ) / np.linalg.norm(j.pos - i.pos)**3 
    return accel

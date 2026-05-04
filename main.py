# Definitions:
#   System: list of bodies
#   Body: class object consisting of physical properties, ie mass, position, volume

import numpy as np
import math
G = 6.6743e-11 # Grav constant: 6.6743 x 10^(-11) m^3/(kg * s^2)

# Body object to be used in equations
class Body:
    def __init__(self, name, mass, pos, velo):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.velo = velo
    force = 0
    accel = 0

def magnitude(vec):
    return np.sqrt(np.sum(vec**2))
    
def gravForceMagnitude(i, j):
    separation = magnitude(i.pos,j.pos)
    return  G * i.mass * j.mass / (separation)**2
    
def unitDirectionVector(i,j):
    direc = j.pos-i.pos
    unit_vec = direc/magnitude(direc)
    return unit_vec

def gravForceVector(i,j):
    separation = j.pos-i.pos
    force = gravForceMagnitude(i,j)
    direction = unitDirectionVector(i,j)
    return force*direction

def calculateForceVectors(system):
    calculatedForces = {}
    for i in system:
        for j in system:
            if i != j:
                hashname = hash("".join(sorted(i.name + j.name)))
                if hashname in calculatedForces:
                    i.force += calculatedForces[hashname] * -1
                else:
                    i.force += gravForceVector(i, j)
                    calculatedForces[hashname] = i.force

def integrator(system, dt):
    calculateForceVectors(system)

    for i in system:
        i.velo += 0.5 * ((i.force/i.mass) + i.accel) * dt
        i.accel = i.force/i.mass
        i.pos += i.velo * dt + 0.5 * i.accel * dt**2

# TODO: write function which generates body from system where the pos is the center of mass of the system 
# Hard part: figuring out when to abstract and unabstract systems


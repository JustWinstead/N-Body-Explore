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
    force = 0

# Newtonian accleration
#   system is a list (or some other data structure) of body objects   
#   i is the specific object we want to get the acceleration of
def newtAcceleration(system, i):
    accel = np.zeros(3) # Array to represent acceleration vector
    for j in system:
        if j == i:
            continue # Guard to prevent divide by zero (if qi = qj, then diff = 0)
        # defining placeholder variables is for cowards
        #F = ma -> a = F/m which cancels its own mass out
        accel += ( G * j.mass ) / (np.linalg.norm(j.pos - i.pos)**2 )
    return accel

def magnitude(vec):
    '''
    The input vector should be an array with x,y,z components
    '''
    return np.sqrt(np.sum(vec**2))
    
def gravForceMagnitude(i, j):
    separation = magnitude(i.pos,j.pos)
    return  G * i.mass * j.mass / (separation)**2
    
def unitDirectionVector(i,j):
    '''
    
    '''
    direc = j.pos-i.pos
    unit_vec = direc/magnitude(direc)
    return unit_vec
def gravForceVector(i,j):
    '''
    
    '''
    separation = j.pos-i.pos
    force = gravForceMagnitude(i,j)
    direction = unitDirectionVector(i,j)
    return force*direction

def calculateForceVector(system):
    calculatedVectors = {}

    for i in range(len(system)):
        for j in range(len(range(system)):
            if i != j:
                hashname = hash("".join(sorted(i.name + j.name)))
                if hashname in calculatedVectors:
                    i.force += calculatedVectors[hashname] * -1
                else:
                    i.force += gravForceVector(i, j)
                    calculatedVectors[hashname] = i.force

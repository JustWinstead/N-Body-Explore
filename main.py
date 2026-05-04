# Definitions:
#   System: list of bodies
#   Body: class object consisting of physical properties, ie mass, position, volume

import numpy as np
import math
G = 6.6743e-11 # Grav constant: 6.6743 x 10^(-11) m^3/(kg * s^2)

# Body object to be used in equations
class Body:
    def __init__(self, name: str, mass: float, pos: np.ndarray, velo: np.ndarray) -> None:
        self.name = name
        self.mass = mass
        self.pos = pos
        self.velo = velo
    force = 0
    accel = 0

def magnitude(vec: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(vec**2))
    
def gravForceMagnitude(i: Body, j: Body) -> np.ndarray:
    separation = magnitude(i.pos,j.pos)
    return  G * i.mass * j.mass / (separation)**2
    
def unitDirectionVector(i: Body, j: Body) -> np.ndarray:
    direc = j.pos-i.pos
    unit_vec = direc/magnitude(direc)
    return unit_vec

def gravForceVector(i: Body, j: Body) -> np.ndarray:
    separation = j.pos-i.pos
    force = gravForceMagnitude(i,j)
    direction = unitDirectionVector(i,j)
    return force*direction

def calculateForceVectors(system) -> None:
    calculatedForces = {}
    for i in system:
        for j in system:
            if i != j:
                hashname = hash("".join(sorted(i.name + j.name)))
                if hashname in calculatedForces:
                    i.force += calculatedForces[hashname] * -1
                else:
                    f = gravForceVector(i, j)
                    i.force += f
                    calculatedForces[hashname] = f

def integrator(system: List[Body], dt: int) -> None:
    calculateForceVectors(system)

    for i in system:
        i.velo += 0.5 * ((i.force/i.mass) + i.accel) * dt
        i.accel = i.force/i.mass
        i.pos += i.velo * dt + 0.5 * i.accel * dt**2

# TODO: write function which generates body from system where the pos is the center of mass of the system 
# Hard part: figuring out when to abstract and unabstract systems

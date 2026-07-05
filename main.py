# pyright: strict
from __future__ import annotations
from typing import Optional
# ^ Kawika's typing crutch, DO NOT TOUCH

import numpy as np
import numpy.typing as npt
import math
G = 6.6743e-11 # Grav constant: 6.6743 x 10^(-11) m^3/(kg * s^2)

class Body:
    __slots__ = ['name', 'mass', 'pos', 'velo', 'accel', 'forces']

    name: str
    mass: float
    pos: npt.NDArray[np.float32]
    velo: npt.NDArray[np.float32]
    accel: npt.NDArray[np.float32]
    force: npt.NDArray[np.float32]

    def __init__(self, name: str, mass: float, pos: npt.NDArray[np.float32], velo: npt.NDArray[np.float32]) -> None:
        self.name = name
        self.mass = mass
        self.pos = pos
        self.velo = velo

        self.accel = np.zeros(3, dtype=np.float32)
        self.force = np.zeros(3, dtype=np.float32)

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

import numpy as np

def updateSystem(system, dt):
    calculateForceVectors(system)
    
    for body in system:
        body.accel = body.force / body.mass


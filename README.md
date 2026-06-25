# N-Body-Explore

An application which models and renders the gravitational interactions of celestial bodies.

## Equations Used:

### Newtonian Acceleration:

$$\ddot{q}\_i = \sum_{j \neq i}^{N} G m_j \frac{q_j - q_i}{ \left\Vert q_j - q_i\right\Vert ^3 }$$

### Newtonian Gravitational Force:

$$F_{21} = -G \frac{m_1 m_2}{ r_{21}^2 } $$

### Optimizations to do:
1. Eliminate unnecessary node subdivision

### Notes
1. Figure out node searching logic
    - Option 1: Space translation, node coord and object coord to object's node coord
    - Option 2: Pass node coord variables to node __init__

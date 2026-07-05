# pyright: strict
from __future__ import annotations
from typing import Optional
# ^ Kawika's typing crutch, DO NOT TOUCH

import numpy as np
import numpy.typing as npt

import main

# important for indexing and iterating through subnodes
# basically creates an 8x3 matrix of vectors for each of 1 and -1
VEC_MATRIX: list[npt.NDArray[np.float32] = [
    np.array([1.0, 1.0, 1.0]),
    np.array([1.0, 1.0, -1.0]),
    np.array([1.0, -1.0, 1.0]),
    np.array([-1.0, 1.0, 1.0]),
    np.array([-1.0, -1.0, 1.0]),
    np.array([-1.0, 1.0, -1.0]),
    np.array([1.0, -1.0, -1.0]),
    np.array([-1.0, -1.0, -1.0]),
]

class Node:
    # locks class dictionary for memory efficiency
    __slots__ = ['com', 'pos', 'body', 'depth', 'nodes', 'size'] 

    com: float
    body: Body
    nodes: list[Node]
    pos: npt.NDArray[np.float32]
    depth: int
    size: float

    # We call this function whenever we want a new node, where all values are calculated
    def __init__(self, pos: npt.NDArray[np.float32], depth: int, size: float):
        self.pos = pos
        self.depth = depth
        self.size = size

        self.com = 0.0
        self.depth = 0
        self.nodes = [None] * 8

    def split(self):
        # We can calculate new node position by doing:
        # pos = (x +- l/2^(d+2), y +- l/2^(d+2), z +- l/2^(d+2))
        # where l is the size value of the node and d is depth + 1 (children are 1 deeper)
        offset = self.size / (1 << (self.depth + 2))
        # bitshift to mimic 2^x ^ 

        for i in range(8):
            # get new coordinates and create new Node
            new_pos = self.pos + (VEC_MATRIX[i] * offset)
            self.nodes[i] = Node(new_pos, self.depth + 1, self.size / 2)


class Tree:
    __slots__ = ['bodies', 'root', 'size']

    bodies: list[main.Body]
    root: Optional[Node]
    size: float

    def __init__(self, system: list[Body]):
        self.bodies = system
        # TODO: calculate from max x, y, and z
        self.size = 0.0
        self.root = None

        for body in bodies:
            self.add(body)

    def add(self, body: Body):
        if self.root is None:
            self.root = Node(np.zeros(3, dtype=np.float32)), 0, self.size)
        
        current = self.root
        while current.body is not None:
            if current.nodes[0] is None:
                current.split()
        
        # TODO: and then some math determining which node to set as current

        current.body = body
        # TODO: calculate center of mass from body mass and position
        current.com = body.mass

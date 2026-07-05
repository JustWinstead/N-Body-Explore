import main

class Node:
    mass = # a numpy array
    pos = # another numpy array
    body = None # Nodes start with zero  
    
    # And then the branch nodes, p means positive, n means negative
    pxpypz = None
    nxpypz = None
    pxnypz = None
    pxpynz = None
    pxnynz = None
    nxpynz = None
    nxnypz = None
    nxnynz = None

    # We call this function whenever we want a new node
    def __init__(coord): # Do we include old node's coordinate?
        self.pos = coord
        # And then we include some math to determine

    def split():
        # Create a new Node for each of the branch node variables

# This keeps track of all data and the root of the tree
class Tree:
    bodies: None # an array of the bodies in the system
    root: None # the root node of the tree

    def ___init__(system): # where system is the array of bodies
        self.bodies = system

        for body in bodies:
            self.add(body)

    def add(body):
        if self.root is None:
            self.root = Node(0) # 0 is a stand-in for a numpy array of the coords (0, 0, 0)
        
        current = self.root
        for current.body is not None:
            if current.pxpypz is None:
                current.split()
            # and then some math determining which node to set as current

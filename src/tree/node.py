import numpy as np


class Node:
    def __init__(self, state, parent=None, action=None, cost=0, visit_time=-1):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.action = action
        self.visit_time = visit_time
        self.children = set()

    
    def __lt__(self, other):
        return self.cost < other.cost

    
    def __str__(self):
        return str(self.state)

    
    def __repr__(self):
        return f"<{str(self.parent)} --{self.action}--> {str(self.state)}. cost: {self.cost} visit time: {self.visit_time}>"


    def __hash__(self):
        return id(self)

    def path(self):
        node, path = self, []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]


    def add_child(self, child):
        self.children.add(child)


""" Árboles Binarios de Búsqueda """
from textwrap import indent


class Node:
    """ Los nodos del árbol """

    def __init__(self, value, function):
        self.value = value
        self.function = function
        self.left = None
        self.right = None


class DecisionTree:
    """ El objeto árbol """

    def __init__(self, root=None):
        self.root = root

    def insert_node(self, node, pivot=None):
        """ Insertar un nodo en el árbol """
        if self.root is None:
            self.root = node
        else:
            if pivot is None:
                pivot = self.root
            if pivot.value > node.value and not pivot.left:
                pivot.left = node
            elif pivot.value > node.value:
                self.insert_node(node, pivot.left)
            elif pivot.value < node.value and not pivot.right:
                pivot.right = node
            elif pivot.value < node.value:
                self.insert_node(node, pivot.right)
            else:
                print(f'Error: node {node.value} already belongs to binary tree')

    def classify(self, img):
        pass

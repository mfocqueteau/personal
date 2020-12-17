""" Árboles Binarios de Búsqueda """
from textwrap import indent


class Node:
    """ Los nodos del árbol """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        text = f'{self.value}.\n'
        repr_children = []
        left = 'Left: '
        left += repr(self.left) if self.left else '-'
        right = 'Right: '
        right += repr(self.right) if self.right else '-'
        repr_children.append(left)
        repr_children.append(right)
        texto_hijos = [indent(child_text, '   ') for child_text in repr_children]
        return text + '\n'.join(texto_hijos)


class BinTree:
    """ El objeto árbol """

    def __init__(self):
        self.root = None

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

    def remove_node(self, value):
        """ Quitar un nodo """
        current = self.root
        found = False
        while not found:
            while value < current.value and current.left:
                current = current.left
            while value > current.value and current.right:
                current = current.right
            found = (value == current.value)
            if not any(current.left, current.right, found):
                return

    def route_node(self, value):
        """ Printea la ruta hasta el nodo de valor 'value' """
        current = self.root
        route = []
        found = False
        while not found:
            while value < current.value and current.left:
                current = current.left
                route.append(current.value)
            while value > current.value and current.right:
                current = current.right
                route.append(current.value)
            found = (value == current.value)
            if not any(current.left, current.right, found):
                return []
        return route

    def __repr__(self):
        return repr(self.root)

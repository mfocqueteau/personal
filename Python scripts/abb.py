from textwrap import indent


class Node:
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
    def __init__(self):
        self.root = None

    def insertNode(self, node, pivot=None):
        if self.root is None:
            self.root = node
        else:
            if pivot is None:
                pivot = self.root
            if pivot.value > node.value and not pivot.left:
                pivot.left = node
            elif pivot.value > node.value:
                self.insertNode(node, pivot.left)
            elif pivot.value < node.value and not pivot.right:
                pivot.right = node
            elif pivot.value < node.value:
                self.insertNode(node, pivot.right)
            else:
                print(f'Error: node {node.value} already belongs to binary tree')

    def removeNode(self, node):
        pass

    def routeNode(self, value):
        current = self.root
        route = []
        found = False
        while not found:
            # Completar
            while value < current.value:
                current = current.left
                route.append(current.value)
            while value > current.value:
                current = current.right
                route.append(current.value)
            found = value == current.value
        return route

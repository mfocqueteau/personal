""" Data structures """
from collections import deque
from typing import Callable, Iterable


Empty = (_ for _ in [])


class stack(list):
    """Stack data structure implementation"""

    def extract(self):
        return self.pop(-1)

    def push(self, *items):
        for item in items:
            self.append(item)


class queue(deque):
    """Queue data structure implementation"""

    def extract(self):
        return self.popleft()

    def push(self, *items):
        for item in items:
            self.append(item)

    def __repr__(self):
        return "[" + ", ".join(x.__repr__() for x in self) + "]"


class Olist(list):
    """Lista que se mantiene ordenada eficientemente"""

    def __init__(
        self,
        iterable: Iterable = Empty,
        key: Callable = lambda x: x,
        reverse: bool = False,
    ):
        super().__init__()
        self.key = key
        self.reverse = reverse
        for element in iterable:
            self.add(element)

    def toggle_reverse(self) -> None:
        """Invertir sentido de la lista"""
        self.reverse = not self.reverse
        self.sort()

    def add(self, element) -> None:
        """Inserción ordenada de números"""
        self.append(element)
        self.sort()

    def sort(self):
        super().sort(key=self.key, reverse=self.reverse)

    def __repr__(self) -> str:
        return f"Olist({super().__repr__()})"

    def __add__(self, other: list) -> list:
        result = Olist(self, self.key, self.reverse)
        for element in other:
            result.add(element)
        return result


class Tree(list):
    """Tree data structure implementation"""

    def __init__(self, content=None, children=None):
        self.content = content
        self._parent = None
        if children:
            super().__init__(children)
            for child in children:
                child.parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        if self._parent:
            self._parent.remove(self)
        self._parent = new_parent

    @property
    def children(self):
        return [*self]

    def push(self, *items):
        for item in items:
            if not isinstance(item, Tree):
                item = Tree(item)
            item.parent = self
            self.append(item)

    def search(self, value, method="bfs"):
        """Search thorugh the tree"""
        if self.content == value:
            return stack((self.content,))
        to_visit = self.build_struct(method)
        while to_visit:
            child = to_visit.extract()
            if child.content == value:
                return child.walk_up()
            to_visit.push(*child)
        return stack()

    def walk_up(self, path=None):
        if not path:
            if self._parent:
                return self._parent.walk_up(stack((self.content,)))[::-1]
            return stack((self.content,))
        path.push(self.content)
        if self._parent:
            return self._parent.walk_up(path)
        return path

    def build_struct(self, method="bfs"):
        struct = queue(self) if method == "bfs" else stack(self) if method == "dfs" else None
        if struct is None:
            raise ValueError("method must be either 'bfs' or 'dfs'")
        return struct

    def walk(self, method="bfs"):
        yield self
        to_visit = self.build_struct(method)
        while to_visit:
            child = to_visit.extract()
            yield child
            to_visit.push(*child)

    def cap(self, value):
        for child in self.walk():
            if child.content == value and child.parent:
                child.parent.remove(child)

    def __repr__(self):
        return self.content.__repr__()

    def __eq__(self, other):
        assert isinstance(other, Tree)
        iter_self, iter_other = self.walk(), other.walk()
        for s, o in zip(iter_self, iter_other):
            if s.value != o.value or not s.__eq__(o):
                return False
        return True

    def __bool__(self):
        return bool(self.content)


class ABB:
    """Binary Search Tree"""

    def __init__(self, content, *children):
        self.content = content
        self.left = None
        self.right = None
        self.type = type(content)
        for child in children:
            self.insert(child)

    @property
    def children(self):
        return self.left, self.right

    def insert(self, *items):
        for item in items:
            item = self.to_abb(item)
            is_left = self.content > item.content
            exists = bool(self.left) if is_left else bool(self.right)
            if is_left and exists:
                self.left.insert(item)
            elif is_left:
                self.left = item
            elif exists:
                self.right.insert(item)
            else:
                self.right = item

    def to_abb(self, item):
        if isinstance(item, ABB):
            type_error = f"can't insert value of type {item.type} into tree of type {self.type}"
            assert isinstance(item.content, self.type), type_error
            return item
        type_error = f"can't insert value of type {type(item)} into tree of type {self.type}"
        assert isinstance(item, self.type), type_error
        return ABB(item)

    def search(self, value):
        path = stack([self.content])
        cur = self
        found = self.content == value
        while not found:
            while value < cur.content:
                if cur.left:
                    cur = cur.left
                    path.push(cur.content)
                else:
                    return stack()
            while value > cur.content:
                if cur.right:
                    cur = cur.right
                    path.push(cur.content)
                else:
                    return stack()
            found = cur.content == value
        return path

    def __repr__(self):
        return str(self.content)

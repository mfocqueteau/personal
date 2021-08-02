""" Data structures """
from collections import deque, defaultdict


class stack(list):
    """ Stack data structure implementation """

    def extract(self):
        return self.pop(-1)

    def push(self, *items):
        for item in items:
            self.append(item)


class queue(deque):
    """ Queue data structure implementation """

    def extract(self):
        return self.popleft()

    def push(self, *items):
        for item in items:
            self.append(item)

    def __repr__(self):
        return '[' + ', '.join(x.__repr__() for x in self) + ']'


class olist(list):
    """ Ordered list implementation """

    def __init__(self, item_type: type, sorting_key=None, reverse=False):
        super().__init__()
        self.type = item_type
        self.reverse = reverse
        self.sorting_key = sorting_key
        self.sort(key=sorting_key, reverse=reverse)

    def add(self, *items):
        for item in items:
            assert isinstance(item, self.type), 'item type doesn\'t match this list type'
            self.append(item)
        self.sort(key=self.sorting_key, reverse=self.reverse)


class Tree(list):
    """ Tree data structure implementation """

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

    def search(self, value, method='bfs'):
        """ Search thorugh the tree """
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

    def build_struct(self, method='bfs'):
        struct = (
            queue(self) if method == 'bfs' else
            stack(self) if method == 'dfs' else
            None
        )
        if struct is None:
            raise ValueError('method must be either \'bfs\' or \'dfs\'')
        return struct

    def walk(self, method='bfs'):
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
    """ Binary Search Tree """

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
            type_error = f'can\'t insert value of type {item.type} into tree of type {self.type}'
            assert isinstance(item.content, self.type), type_error
            return item
        type_error = f'can\'t insert value of type {type(item)} into tree of type {self.type}'
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


class HashTable(defaultdict):
    """ Hashed table implementation """

    def __init__(self, length):
        super().__init__(stack)
        self.length = length

    def store(self, value):
        self[self.get_key(value)].push(value)

    def hash(self, value):
        assert isinstance(value, (int, float))
        return int((value**2 / 3) % self.length)

    def get_key(self, value):
        return self.hash(value)

    def __repr__(self):
        return '{\n' + '\n'.join(f'  {key}: {value}' for key, value in self.items()) + '\n}'

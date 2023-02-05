from typing import Union
from binary_node import Node


class BinarySearchTree:

    def __init__(self) -> None:
        self.__root = None

    @property
    def root(self):
        if self.__root is not None:
            return self.__root
        else:
            return None

    @root.setter
    def root(self, value):
        if value.__class__ == Node.__class__ or value is not None:
            self.__root = value

    def insert(self, z):
        node = Node(z)
        x = self.root
        y = None
        if self.root is None:
            self.root = node
            return
        while x is not None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

    def tree_minimum(self, x) -> Node:
        while x.left is not None:
            x = x.left
        return x

    def tree_maximum(self, x) -> Node:
        while x.right is not None:
            x = x.right
        return x

    def tree_search(self, value) -> Node:
        x = self.root
        while x is not None and value != x.value:

            if value < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_tree_walk(self, x: Union["Node", None]):
        if x is not None:
            self.inorder_tree_walk(x.left)
            print(x.value)
            self.inorder_tree_walk(x.right)

    def transplant(self, u: Node, v: Node):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        node = self.tree_search(z)
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.tree_minimum(node.right)
            if y != node.right:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


tree = BinarySearchTree()
tree.insert(9)
print(tree.root)
tree.insert(4)
tree.insert(5)
tree.insert(10)
print(tree.root)
tree.inorder_tree_walk(tree.root)
print(tree.root)
print(tree.tree_search(5))
print("----------------")
tree.tree_delete(4)
tree.insert(14)
tree.insert(52)
tree.insert(100)
tree.insert(41)
tree.insert(53)
tree.insert(108)


tree.display()
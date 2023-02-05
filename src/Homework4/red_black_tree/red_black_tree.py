from red_black_node import Node


class RedBlackTree:
    def __init__(self):
        self.nil = Node()
        self.root = self.nil

    def insert(self, value):
        node = Node(value)
        node.parent = None
        node.left = self.nil
        node.right = self.nil
        node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if node.value < current.value:
                current = current.left
            elif node.value > current.value:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        # Fix the tree
        self.fix_insert(node)

    def tree_minimum(self, x) -> Node:
        while x.left != self.nil:
            x = x.left
        return x

    def tree_maximum(self, x) -> Node:
        while x.right != self.nil:
            x = x.right
        return x

    def fix_insert(self, node):
        while node != self.root and node.parent.red:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_left(node.parent.parent)
            else:
                u = node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_right(node.parent.parent)
        self.root.red = False

    def search(self, val):
        curr = self.root
        while curr != self.nil and val != curr.value:
            if val < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def transplant(self, u: Node, v: Node):
        if u.parent is self.nil or u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def tree_delete(self, z):
        node = self.search(z)
        print(node)
        node_original_color = node.red
        if node.left is self.nil:
            x = node.right
            self.transplant(node, node.right)
        elif node.right is self.nil:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.tree_minimum(node.right)
            print("y", y)
            node_original_color = y.red
            x = y.right
            if y != node.right:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            else:
                x.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.red = node.red
        if not node_original_color:
            self.delete_fix(x)

    def delete_fix(self, x: Node):
        while x != self.root and x.red is False:
            if x == x.parent.left:
                w = x.parent.right
                if w.red is True:
                    w.red = False
                    x.parent.red = True
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.red is False and w.right.red is False:
                    w.red = True
                    x = x.parent
                else:
                    if w.right.red is False:
                        w.left.red = False
                        w.red = False
                        self.rotate_right(w)
                        w = x.parent.right
                    w.red = x.parent.red
                    x.parent.red = False
                    w.right.red = False
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.red is True:
                    w.red = False
                    x.parent.red = True
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.red is False and w.left.red is False:
                    w.red = True
                    x = x.parent
                else:
                    if w.left.red is False:
                        w.right.red = False
                        w.red = False
                        self.rotate_left(w)
                        w = x.parent.left
                    w.red = x.parent.red
                    x.parent.red = False
                    w.left.red = False
                    self.rotate_right(x.parent)
                    x = self.root
        x.red = False

    def __repr__(self):
        return '\n'.join(self.display())

    def display(self):
        lines, *_ = self._display_aux(self.root)
        return lines

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '{} ({})'.format(node.value, "r" if node.red else 'b')
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '{} ({})'.format(node.value, "r" if node.red else 'b')
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '{} ({})'.format(node.value, "r" if node.red else 'b')
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '{} ({})'.format(node.value, "r" if node.red else 'b')
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

tree = RedBlackTree()

tree.insert(9)
tree.insert(4)
tree.insert(5)
tree.insert(10)
tree.insert(14)
tree.insert(52)
tree.insert(100)
tree.insert(41)
tree.insert(53)
tree.insert(108)

print(tree.search(10))
print(tree)
tree.tree_delete(10)
print(tree)
tree.tree_delete(53)
print(tree)
tree.tree_delete(14)
print(tree)
class Node:
    def __init__(self, value = None):
        self.__red = None
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__value = value

    def __repr__(self) -> str:
        return "Parent: {}\nLeft: {}\nRight: {}\nValue: {}\nColor: {}". \
            format(self.parent.value if self.parent is not None else None,
                   self.left.value if self.left is not None else None,
                   self.right.value if self.right is not None else None,
                   self.value,
                   "red" if self.red else 'black')

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, value: bool):
        self.__red = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        if parent.__class__ == self.__class__ or parent is None:
            self.__parent = parent
        else:
            self.__parent = Node(parent)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if right.__class__ == self.__class__ or right is None:
            self.__right = right
        else:
            self.__right = Node(right)

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if left.__class__ == self.__class__ or left is None:
            self.__left = left
        else:
            self.__left = Node(left)

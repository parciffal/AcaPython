from typing import Union


class Node:
    def __init__(self, value: None):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__value = value
    
    """def __eq__(self, __o: "Node") -> bool:
        return self.value == __o.value
        
    def __ne__(self, __o: "Node") -> bool:
        return not self.value == __o.value

    def __lt__(self, __o: "Node") -> bool:
        return self.value < __o.value

    def __le__(self, __o: "Node"):
        if self.value is not None and __o.value is not None:
            return self.value <= __o.value
        if self.value is None:
            return True
        if __o.value is None:
            return False

    def __gt__(self, __o: "Node") -> bool:
        return self.value > __o.value

    def __ge__(self, __o: "Node"):
        if self.value is not None and __o.value is not None:
            return self.value >= __o.value
        if self.value is None:
            return False
        if __o.value is None:
            return True"""

    def __repr__(self) -> str:
        return "Parent: {}\nLeft: {}\nRight: {}\nValue: {}".\
               format(self.parent.value if self.parent is not None else None,
                      self.left.value if self.left is not None else None,
                      self.right.value if self.right is not None else None,
                      self.value)

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

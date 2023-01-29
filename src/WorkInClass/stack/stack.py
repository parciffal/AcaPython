class Node:
    def __init__(self, value: int, prew: "self"):
        self.value = value
        self.prew = prew

    def __repr__(self):
        return "Value: {}\n Prew: {}".format(self.value, self.prew)


class Stack:
    __top: Node

    def __init__(self):
        self.__top = None

    def empty(self):
        if self.__top is None:
            return True
        return False

    def push(self, a):
        if self.empty():
            self.__top = Node(a, None)
        else:
            node = Node(a, self.__top)
            self.__top = node

    def pop(self):
        if self.__top.prew is None:
            top = self.__top.value
            self.__top = None
            return top
        else:
            prew = self.__top.prew
            top = self.__top.value
            self.__top = prew
            return top

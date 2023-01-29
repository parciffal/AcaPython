import dataclasses


class Node:
    def __init__(self, value, next: 'Node' = None, prew: 'Node' = None):
        self.next = next
        self.prew = prew
        self.value = value

    def __repr__(self):
        return self.value



class IndexOutOfRange(Exception):
    def __init__(self, index, len):
        super().__init__("Index out of range Index: {}  Len: {}".format(index, len))


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    def __len__(self):
        node = self.first
        count = 0
        while node != self.last:
            count += 1
            node = self.first.next

    def __repr__(self):
        i = []
        node = self.first
        while node != self.last:
            i.append(node.value)
        return "{}".format(i)

    def delete(self, index: int):
        if index >= len(self):
            raise IndexOutOfRange(index, len(self))
        count = 0
        node = self.first
        while count <= len(self):
            node = node.next
            if count == index:
                next = node.next
                prew = node.prew
                next.prew = prew
                prew.next = next
                break

    def search(self, value):
        node = self.first
        while node != self.last:
            if node.value == value:
                return node
            node = node.next
        return None

    def insert(self, value, index):
        if index >= len(self):
            raise IndexOutOfRange(index, len)
        count = 0
        node = self.first
        while count <= index:
            if count == index:
                next = node.next
                prew = node
                new_node = Node(value, next, prew)
            node = node.next




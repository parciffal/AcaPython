from queue_exceptions import *

class Queue:
    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def __repr__(self):
        return "Queue: {}".format(self.__queue)

    def enqueue(self, x: int):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)


queue = Queue()

for i in range(12, 39):
    queue.enqueue(i)

print(queue)

for i in range(len(queue)):
    queue.dequeue()

print(queue)
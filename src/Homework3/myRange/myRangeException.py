class StopIterationMy(Exception):
    def __init__(self):
        super().__init__("Iteration Ended")

class IndexOutOfRange(Exception):
    def __init__(self, i, l) -> None:
        super().__init__("Index out of Range: Len: {} Index: {}".format(l, i))

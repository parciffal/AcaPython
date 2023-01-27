class StopIterationMy(Exception):
    def __init__(self):
        super().__init__("Iteration Ended")

class InvalidInputException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Invalid Input's\ncurrent: {} end: {} step: {}".format(args[0], args[1], args[2]))


class IndexOutOfRange(Exception):
    def __init__(self, i, l) -> None:
        super().__init__("Index out of Range: Len: {} Index: {}".format(l, i))

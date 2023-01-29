from .abc_list import ABCList


class Factory(ABCList):

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

    def create_list(self, type: "Factory"):
        return type

    def add(self):
        pass

    def pop(self):
        pass

    def search(self):
        pass


from ..factory import Factory


class LinkedList(Factory):
    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

    def create_list(self):
        return self

    def add(self):
        super().add()

    def pop(self):
        super().pop()

    def search(self):
        super().search()
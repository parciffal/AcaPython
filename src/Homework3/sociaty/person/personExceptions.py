class AgeOutOfRange(Exception):
    def __init__(self, age: int) -> None:
        super().__init__("Age out range 0 .. 150 : {}".format(age))
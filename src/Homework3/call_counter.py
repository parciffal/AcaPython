class CallCounter:
    def __init__(self, func):
        self.__count = 0
        self.__func = func
    
    def __call__(self, *args, **kwds):
        self.count += 1
        print(self)
        return self.func(*args, **kwds)

    def __repr__(self) -> str:
        return "Function {} called {} times"\
               .format(self.func.__name__, self.count)
    
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count
    
    @property
    def func(self):
        return self.__func

    @func.setter
    def func(self, value):
        self.__func = value



@CallCounter
def function1():
    pass

function1()
function1()

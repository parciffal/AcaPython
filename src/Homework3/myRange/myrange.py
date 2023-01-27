from myRangeException import StopIterationMy, IndexOutOfRange

class MyRange:
    """
        Class MyRange
        
        Data members:
        1. current
        2. end
        3. step

        Data methods:
        1. __init__
        2. __repr__
        3. __iter__
        4. __next__
        5. __len__
        6. __getitem__ 
        7. __reversed__
    
    """

    def __init__(self, end: int,current: int = 0, step: int = 1):
        self.__current = current
        self.__end = end
        self.__step = step
    
    def __len__(self):
        return int((self.end - self.current)/self.step)

    def __repr__(self) -> str:
        return "Range from {} to {} with step {}".format(self.current, self.end, self.step)
    
    def __iter__(self):
        return self
    
    def __reversed__(self):
       self.current, self.end = self.end, self.current
       self.step = -1*self.step
       return self

    def __next__(self):
        if self.step < 0 and self.current > self.end:
            raise StopIteration
        if not hasattr(self, 'iter_value'):
            self.iter_value = self.current

            yield self.iter_value
        else:
            if self.step >= 0:
                while self.iter_value <= self.end:
                    self.iter_value += self.step
                    if self.iter_value <= self.end:
                        yield self.iter_value
            else:
                while self.iter_value >= self.end:
                    self.iter_value += self.step
                    if self.iter_value >= self.end:
                        yield self.iter_value

            raise StopIterationMy

    def __getitem__(self, index):
        if index >= self.__len__() or index*-1 >= self.__len__() :
            raise IndexOutOfRange(index, self.__len__())
        value = self.current
        if index < 0:
            index = self.__len__() + index
        count = 0
        while count <= index:
            value += self.step
            count += 1
        return value

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, value: int):
        self.__current = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value: int):
        self.__end = value

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, value: int):
        self.__step = value


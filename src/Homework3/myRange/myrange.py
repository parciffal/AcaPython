class Range:
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

    def __init__(self, current: int, end: int, step: int):
        self.__current = current
        self.__end = end
        self.__step = step
    
    def __len__(self):
        return int((self.end - self.current)/self.step)

    def __repr__(self) -> str:
        return "Range from {} to {} with step {}".format(self.current, self.end, self.step)
    
    def __iter__(self):
        self.iter_value = self.current
        while self.iter_value < self.end:
            yield self.iter_value
            self.iter_value += self.step
    
    def __reversed__(self):
        self.reversed_value = self.end
        while self.reversed_value > self.current:
            yield self.reversed_value
            self.reversed_value -= self.step

    def __next__(self): 
        return next(self)

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


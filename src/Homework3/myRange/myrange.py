from myRangeException import StopIterationMy, IndexOutOfRange, InvalidInputException

class MyRange:

    def __init__(self, current: int, end: int, step: int):
        if self.check_inputs(current, end, step):
            self.__current = current
            self.__end = end
            self.__step = step
        else:
            raise InvalidInputException(current, end, step)
    
    def check_inputs(self, current, end, step):
        if current > end and step > 0:
            return False
        if current < end and step < 0:
            return False
        if step == 0:
            return False
        return True
    
    def __call__(self, current: int, end: int, step: int):
        if not self.check_inputs(current, end, step):
            raise InvalidInputException(current, end, step)
        else:
            arr = []
            if step >= 0:
                while current < end:
                    arr.append(current)
                    current += step
                    
            else:
                while current > end:
                    arr.append(current)
                    current += step
            return arr



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
        if self.step < 0:
            if self.current < self.end:
                raise StopIteration
        if not hasattr(self, 'iter_value'):
            self.iter_value = self.current

            yield self.iter_value
        else:
            if self.step >= 0:
                while self.iter_value < self.end:
                    self.iter_value += self.step
                    if self.iter_value < self.end:
                        yield self.iter_value
            else:
                while self.iter_value > self.end:
                    self.iter_value += self.step
                    if self.iter_value > self.end:
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
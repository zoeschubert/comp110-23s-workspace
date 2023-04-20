"""Practice for QZ03."""

class Square:

    width: int
    length: int

    def __init__(self, inp_width: int, inp_length: int):
        self.width = inp_width
        self.length = inp_length

    def __mul__(self, times: int) -> Square:
        new_width: int = self.width * times
        new_length: int = self.length * times
        return Square(new_width, new_length)
    
    def __add__(self, extra: int) -> Square:
        self.width += extra
        self.length += extra
        return Square
    
    def resize(self, new_width: int, new_length: int):
        self.width = new_width
        self.length = new_length

    def area(self) -> int:
        area: int
        area = self.width * self.length
        return area



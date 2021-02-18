class Quadrilateral:

    def __init__(self, x, y):

        self.x = x
        self.y = y

class Trapezoid(Quadrilateral):

    def __init__(self, x, y, TrapHeight):
        Quadrilateral.__init__(self, x, y)
        
        self.TrapHeight = TrapHeight

    def AreaTrapezoid(self):

        areaTrapezoid = 0.5 * (self.x + self.y) * self.TrapHeight

        return areaTrapezoid

class Parallelogram(Quadrilateral):

    def __init__(self, x, y, ParaHeight):
        Quadrilateral.__init__(self, x, y)

        self.ParaHeight = ParaHeight

    def AreaParallelogram(self):

        areaParallelogram = self.x * self.ParaHeight

        return areaParallelogram

class Rectangle(Quadrilateral):

    def __init__(self, x, y):
        Quadrilateral.__init__(self, x, y)

    def AreaRectangle(self):

        areaRectangle = self.x * self.y

        return areaRectangle

class Square(Quadrilateral):

    def __init__(self, x, y):
        Quadrilateral.__init__(self, x, y)

    def AreaSquare(self):

        areaSquare = self.x ** 2

        return areaSquare
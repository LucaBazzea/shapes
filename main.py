from shape import Quadrilateral, Trapezoid, Parallelogram, Rectangle, Square

def Main():

    Trapezoid1 = Trapezoid(5, 7, 6)
    Parallelogram1 = Parallelogram(4, 5, 7)
    Rectangle1 = Rectangle(6, 10)
    Square1 = Square(4, 4)

    print(f"Area of Trapezoid: {Trapezoid1.AreaTrapezoid()}")
    print(f"Area of Parallelogram {Parallelogram1.AreaParallelogram()}")
    print(f"Area of Rectangle: {Rectangle1.AreaRectangle()}")
    print(f"Area of Square: {Square1.AreaSquare()}")

if __name__=="__main__":

    Main()
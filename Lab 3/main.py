
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        return Vector(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        return Vector(self.__x / other, self.__y / other)

    def print_vector(self):
        print("x = ", self.__x, " y = ", self.__y)


vector1 = Vector(1,2)
print("vector 1:")
vector1.print_vector()

vector2 = Vector(4,6)
print("vector 2:")
vector2.print_vector()

vector3 = vector1 + vector2

print("vector 1 + vector 2:")
vector3.print_vector()

vector3 = vector1 - vector2
print("vector 1 - vector 2:")
vector3.print_vector()

vector3 = vector1 * 5
print("vector 1 * 5:")
vector3.print_vector()

vector3 = vector1 / 5
print("vector 1 / 5:")
vector3.print_vector()


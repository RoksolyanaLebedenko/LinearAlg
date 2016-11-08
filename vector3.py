from math import sqrt


class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        squared_magnitude = self.sqremagnitude
        self.x = self.x / squared_magnitude
        self.y = self.y / squared_magnitude
        self.z = self.z / squared_magnitude

    @property
    def normalized(self):
        squared_magnitude = self.sqremagnitude
        return Vector3(self.x / squared_magnitude, self.y / squared_magnitude, self.z / squared_magnitude)

    @property
    def sqremagnitude(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    @property
    def magnitude(self):
        return sqrt(self.sqremagnitude)

    def __add__(self, other):
        if isinstance(other, Vector3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise TypeError("Can't add this to Vector3")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            raise TypeError("Can't sub this from Vector3")

    def __mul__(self, other):
        if isinstance(other, Vector3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            raise TypeError("Can't multiply this with Vector3")

    def __truediv__(self, other):
        if isinstance(other, Vector3):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            raise TypeError("Can't divide Vector3")

    def __floordiv__(self, other):
        if isinstance(other, Vector3):
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z
        else:
            raise TypeError("Can't divide Vector3")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __eq__(self, other):
        if isinstance(other, Vector3):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
        return False

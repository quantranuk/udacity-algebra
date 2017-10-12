import math


class Vector:

    coordinates = []

    def __init__(self, new_coordinates):
        self.coordinates = new_coordinates

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalized(self):
        magnitude = self.magnitude()
        if not magnitude:
            raise Exception("Cannot normalize the zero vector")
        return Vector(self.times_scalar(1 / magnitude))

    def dot(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_rad(self, v):
        magnitude_multiplied = self.magnitude() * v.magnitude()
        if not magnitude_multiplied:
            raise Exception("Cannot find angle of the zero vector")
        return math.acos(self.dot(v) / magnitude_multiplied)

    def angle_degree(self, v):
        return self.angle_rad(v) * 180 / math.pi

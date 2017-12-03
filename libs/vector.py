from libs.float_utils import is_zero as float_is_zero
import math


class Vector(object):

    coordinates = []
    current = 0

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.current = 0

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def is_zero(self):
        return float_is_zero(self.magnitude())

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
        return self.times_scalar(1 / magnitude)

    def dot(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_rad(self, v):
        magnitude_multiplied = self.magnitude() * v.magnitude()
        if not magnitude_multiplied:
            raise Exception("Cannot find angle of the zero vector")
        return math.acos(self.dot(v) / magnitude_multiplied)

    def angle_degree(self, v):
        return self.angle_rad(v) * 180 / math.pi

    def is_parallel(self, v):
        self_magnitude = self.magnitude()
        v_magnitude = v.magnitude()
        if float_is_zero(self_magnitude) or float_is_zero(v_magnitude):
            return True
        else:
            return float_is_zero(abs(abs(self.dot(v)) - abs(self_magnitude * v_magnitude)))

    def is_orthogonal(self, v):
        return float_is_zero(abs(self.dot(v)))

    def component_parallel_to(self, v):
        if v.is_zero():
            raise Exception("Cannot find parallel component of zero vector")
        v_normalized = v.normalized()
        return v_normalized.times_scalar(self.dot(v_normalized))

    def component_orthogonal_to(self, v, parallel_component=None):
        if v.is_zero():
            raise Exception("Cannot find parallel component of zero vector")
        if parallel_component is None:
            parallel_component = self.component_parallel_to(v)
        return self.minus(parallel_component)

    def cross(self, v):
        x = self.coordinates[1] * v.coordinates[2] - v.coordinates[1] * self.coordinates[2]
        y = -(self.coordinates[0] * v.coordinates[2] - v.coordinates[0] * self.coordinates[2])
        z = self.coordinates[0] * v.coordinates[1] - v.coordinates[0] * self.coordinates[1]
        return Vector([x, y, z])

    def __iter__(self):
        return self.coordinates.__iter__()

    def __getitem__(self, item):
        return self.coordinates.__getitem__(item)

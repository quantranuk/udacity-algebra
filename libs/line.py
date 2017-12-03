from libs.float_utils import is_zero as float_is_zero
from libs.vector import Vector


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    COINCIDENT_VECTOR = 'Vector is coincident'

    dimension = 2
    normal_vector = Vector([0.0]*dimension)
    constant_term = 0.0
    base_point = None

    def __init__(self, normal_vector=None, constant_term=None):
        self.normal_vector = normal_vector
        self.constant_term = constant_term
        self.set_basepoint()

    def __eq__(self, other):
        if self.normal_vector.is_zero():
            if other.normal_vector.is_zero():
                return self.constant_term == other.constant_term
            else:
                return False
        elif other.normal_vector.is_zero():
            return False
        else:
            return self.is_coincident(other)

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            base_point_coordinates = [0.0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            base_point_coordinates[initial_index] = c/initial_coefficient
            self.base_point = Vector(base_point_coordinates)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.base_point = None
            else:
                raise e

    def is_parallel(self, ln):
        return self.normal_vector.is_parallel(ln.normal_vector)

    def get_intersection(self, ln):

        if self.normal_vector.is_zero() or ln.normal_vector.is_zero():
            return None

        if self.is_parallel(ln):
            if self.is_coincident(ln, True):
                raise Exception(self.COINCIDENT_VECTOR)
            else:
                return None
        a, b = self.normal_vector.coordinates
        c, d = ln.normal_vector.coordinates
        k1 = self.constant_term
        k2 = ln.constant_term
        base = a*d - b*c
        x = (d*k1 - b*k2) / base
        y = (-c*k1 + a*k2) / base
        return Vector([x, y])

    def is_coincident(self, ln, is_parallel_proven=False):
        if not is_parallel_proven:
            is_parallel_proven = self.is_parallel(ln)

        if not is_parallel_proven:
            return False

        two_base_points = self.base_point.minus(ln.base_point)
        return two_base_points.is_orthogonal(self.normal_vector)

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not float_is_zero(item):
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

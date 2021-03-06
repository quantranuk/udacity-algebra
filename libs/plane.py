from libs.float_utils import is_zero as float_is_zero
from libs.vector import Vector


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    dimension = 3
    normal_vector = Vector([0.0] * dimension)
    constant_term = 0.0
    basepoint = Vector([0.0]*dimension)

    def __init__(self, normal_vector=None, constant_term=None):
        if normal_vector:
            self.normal_vector = normal_vector
        if constant_term:
            self.constant_term = constant_term
        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0.0]*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

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
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i+1)
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

    def is_parallel(self, pl):
        return self.normal_vector.is_parallel(pl.normal_vector)

    def __eq__(self, other):
        if self.normal_vector.is_zero():
            if other.normal_vector.is_zero():
                return self.constant_term == other.constant_term
            else:
                return False
        elif other.normal_vector.is_zero():
            return False
        elif not self.is_parallel(other):
            return False
        else:
            test_vector = self.basepoint.minus(other.basepoint)
            return test_vector.is_orthogonal(self.normal_vector)

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not float_is_zero(item):
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

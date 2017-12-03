from libs.float_utils import is_zero as float_is_zero
from libs.plane import Plane
from copy import deepcopy


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        plane = self.planes[row]
        new_normal_vector = plane.normal_vector.times_scalar(coefficient)
        new_constant_term = plane.constant_term * coefficient
        self.planes[row] = Plane(new_normal_vector, new_constant_term)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        p1 = self.planes[row_to_add]
        p2 = self.planes[row_to_be_added_to]
        new_normal_vector = p1.normal_vector.times_scalar(coefficient).plus(p2.normal_vector)
        new_constant_term = (p1.constant_term * coefficient) + p2.constant_term
        self.planes[row_to_be_added_to] = Plane(new_normal_vector, new_constant_term)

    def compute_triangular_form(self):
        system = deepcopy(self)
        num_planes = len(system.planes)
        j = 0
        for i in range(num_planes):
            while j < system.dimension:
                plane = system.planes[i]
                c = plane.normal_vector.coordinates[j]
                if float_is_zero(c):
                    r = system.get_first_row_below_with_non_zero_coefficient(i, j)
                    if r is None:
                        j += 1
                        continue
                    else:
                        system.swap_rows(i, r)
                        plane = system.planes[i]
                        c = plane.normal_vector.coordinates[j]
                system.clear_all_terms_below_with_non_zero_coefficient(i, j, c)
                j += 1
                break
        return system

    def get_first_row_below_with_non_zero_coefficient(self, i, j):
        for row in range(i + 1, len(self.planes)):
            if not float_is_zero(self.planes[row].normal_vector.coordinates[j]):
                return row
        return None

    def clear_all_terms_below_with_non_zero_coefficient(self, from_row, variable_no, coefficient):
        for row in range(from_row + 1, len(self.planes)):
            coefficient_to_clear = self.planes[row].normal_vector.coordinates[variable_no]
            if not float_is_zero(coefficient_to_clear):
                self.add_multiple_times_row_to_row(-coefficient_to_clear/coefficient, from_row, row)

    def clear_all_terms_above_with_non_zero_coefficient(self, from_row, variable_no, coefficient = 1):
        for row in reversed(range(from_row)):
            coefficient_to_clear = self.planes[row].normal_vector.coordinates[variable_no]
            if not float_is_zero(coefficient_to_clear):
                self.add_multiple_times_row_to_row(-coefficient_to_clear/coefficient, from_row, row)

    def compute_rref(self):
        tf = self.compute_triangular_form()
        for i in reversed(range(len(tf.planes))):
            plane = tf.planes[i]
            for j in range(tf.dimension):
                coefficient = plane.normal_vector.coordinates[j]
                if float_is_zero(coefficient):
                    continue
                if coefficient != 1:
                    new_normal_vector = plane.normal_vector.times_scalar(1 / coefficient)
                    new_constant_term = plane.constant_term / coefficient
                    tf.planes[i] = Plane(new_normal_vector, new_constant_term)
                tf.clear_all_terms_above_with_non_zero_coefficient(i, j)
                break
        return tf

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

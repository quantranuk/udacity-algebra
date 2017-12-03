from libs.vector import Vector
from libs.plane import Plane
from libs.linsys import LinearSystem

p0 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p1 = Plane(normal_vector=Vector([0, 1, 0]), constant_term=2)
p2 = Plane(normal_vector=Vector([1, 1, -1]), constant_term=3)
p3 = Plane(normal_vector=Vector([1, 0, -2]), constant_term=2)

s = LinearSystem([p0, p1, p2, p3])
s.swap_rows(0, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 1 failed')

s.swap_rows(1, 3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print('test case 2 failed')

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 3 failed')

s.multiply_coefficient_and_row(1, 0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 4 failed')

s.multiply_coefficient_and_row(-1, 2)
if not (s[0] == p1 and
                s[1] == p0 and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), constant_term=-3) and
                s[3] == p3):
    print('test case 5 failed')

s.multiply_coefficient_and_row(10, 1)
if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10, 10, 10]), constant_term=10) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), constant_term=-3) and
                s[3] == p3):
    print('test case 6 failed')

s.add_multiple_times_row_to_row(0, 0, 1)
if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10, 10, 10]), constant_term=10) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), constant_term=-3) and
                s[3] == p3):
    print('test case 7 failed')

s.add_multiple_times_row_to_row(1, 0, 1)
if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10, 11, 10]), constant_term=12) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), constant_term=-3) and
                s[3] == p3):
    print('test case 8 failed')

s.add_multiple_times_row_to_row(-1, 1, 0)
if not (s[0] == Plane(normal_vector=Vector([-10, -10, -10]), constant_term=-10) and
                s[1] == Plane(normal_vector=Vector([10, 11, 10]), constant_term=12) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), constant_term=-3) and
                s[3] == p3):
    print('test case 9 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([0, 1, 1]), constant_term=2)
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
                t[1] == p2):
    print('test case 10 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=2)
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
                t[1] == Plane(constant_term=1)):
    print('test case 11 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([0, 1, 0]), constant_term=2)
p3 = Plane(normal_vector=Vector([1, 1, -1]), constant_term=3)
p4 = Plane(normal_vector=Vector([1, 0, -2]), constant_term=2)
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
                t[1] == p2 and
                t[2] == Plane(normal_vector=Vector([0, 0, -2]), constant_term=2) and
                t[3] == Plane()):
    print('test case 12 failed')

p1 = Plane(normal_vector=Vector([0, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([1, -1, 1]), constant_term=2)
p3 = Plane(normal_vector=Vector([1, 2, -5]), constant_term=3)
s = LinearSystem([p1, p2, p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(normal_vector=Vector([1, -1, 1]), constant_term=2) and
                t[1] == Plane(normal_vector=Vector([0, 1, 1]), constant_term=1) and
                t[2] == Plane(normal_vector=Vector([0, 0, -9]), constant_term=-2)):
    print('test case 13 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([0, 1, 1]), constant_term=2)
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([1, 0, 0]), constant_term=-1) and
                r[1] == p2):
    print('test case 14 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=2)
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == p1 and
                r[1] == Plane(constant_term=1)):
    print('test case 15 failed')

p1 = Plane(normal_vector=Vector([1, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([0, 1, 0]), constant_term=2)
p3 = Plane(normal_vector=Vector([1, 1, -1]), constant_term=3)
p4 = Plane(normal_vector=Vector([1, 0, -2]), constant_term=2)
s = LinearSystem([p1, p2, p3, p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([1, 0, 0]), constant_term=0) and
                r[1] == p2 and
                r[2] == Plane(normal_vector=Vector([0, 0, -2]), constant_term=2) and
                r[3] == Plane()):
    print('test case 16 failed')

p1 = Plane(normal_vector=Vector([0, 1, 1]), constant_term=1)
p2 = Plane(normal_vector=Vector([1, -1, 1]), constant_term=2)
p3 = Plane(normal_vector=Vector([1, 2, -5]), constant_term=3)
s = LinearSystem([p1, p2, p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([1, 0, 0]), constant_term=23.0/9.0) and
                r[1] == Plane(normal_vector=Vector([0, 1, 0]), constant_term=7.0/9.0) and
                r[2] == Plane(normal_vector=Vector([0, 0, 1]), constant_term=2.0/9.0)):
    print('test case 17 failed')


p1 = Plane(normal_vector=Vector([5.862, 1.178, -10.366]), constant_term=-8.15)
p2 = Plane(normal_vector=Vector([1, -1, 1]), constant_term=2)
p3 = Plane(normal_vector=Vector([1, 2, -5]), constant_term=3)
s = LinearSystem([p1, p2, p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([1, 0, 0]), constant_term=23.0/9.0) and
                r[1] == Plane(normal_vector=Vector([0, 1, 0]), constant_term=7.0/9.0) and
                r[2] == Plane(normal_vector=Vector([0, 0, 1]), constant_term=2.0/9.0)):
    print('test case 18 failed')

p1 = Plane(Vector([5.862, 1.178, -10.366]), -8.15)
p2 = Plane(Vector([-2.931, -0.589, 5.183]), -4.075)
s = LinearSystem([p1, p2])
print('')
print(s.compute_rref())

p1 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
p2 = Plane(Vector([4.315, 11.132, -5.27]), -6.775)
p3 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)
s = LinearSystem([p1, p2, p3])
print('')
print(s.compute_rref())

p1 = Plane(Vector([5.262, 2.734, -9.878]), -3.441)
p2 = Plane(Vector([5.111, 6.358, 7.638]), -2.152)
p3 = Plane(Vector([2.016, -9.924, -1.367]), -9.278)
p4 = Plane(Vector([2.167, -13.543, -18.883]), -10.567)
s = LinearSystem([p1, p2, p3, p4])
print('')
print(s.compute_rref())

p1 = Plane(Vector([0.786, 0.786, 0.588]), -0.714)
p2 = Plane(Vector([-0.138, -0.138, 0.244]), 0.319)
s = LinearSystem([p1, p2])
print('')
print(s.compute_rref())


p1 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
p2 = Plane(Vector([4.315, 11.132, -5.27]), -6.775)
p3 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)
s = LinearSystem([p1, p2, p3])
print('')
print(s.compute_rref())

p1 = Plane(Vector([0.935, 1.76, -9.365]), -9.955)
p2 = Plane(Vector([0.187, 0.352, -1.873]), -1.991)
p3 = Plane(Vector([0.374, 0.704, -3.746]), -3.982)
p4 = Plane(Vector([-0.561, -1.056, 5.619]), 5.973)
s = LinearSystem([p1, p2, p3, p4])
print('')
print(s.compute_rref())


import libs.algebra as algebra

vector_1 = algebra.Vector([7.887, 4.138])
vector_2 = algebra.Vector([-8.802, 6.776])
print(vector_1.dot(vector_2))

vector_3 = algebra.Vector([-5.955, -4.904, -1.874])
vector_4 = algebra.Vector([-4.496, -8.755, 7.103])
print(vector_3.dot(vector_4))

vector_5 = algebra.Vector([3.183, -7.627])
vector_6 = algebra.Vector([-2.668, 5.319])
print(vector_5.angle_rad(vector_6))

vector_7 = algebra.Vector([7.35, 0.221, 5.188])
vector_8 = algebra.Vector([2.751, 8.259, 3.985])
print(vector_7.angle_degree(vector_8))

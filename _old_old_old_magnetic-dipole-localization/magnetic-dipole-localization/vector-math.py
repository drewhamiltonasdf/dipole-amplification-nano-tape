from sympy.vector import CoordSys3D, Del, is_conservative, is_solenoidal, ParametricRegion, vector_integrate, ImplicitRegion
from sympy import sin, cos, exp, pi, symbols, Eq
from sympy.abc import r, x, y, z, theta, phi
import numpy as np

R = CoordSys3D('R')
m = 1*R.i + 1*R.j + 1*R.k               # units of A*m^2

field = R.x*R.i + R.y*R.j + R.z*R.k

vacuum_permittivity = 1.256   # units of kg * m * A^-2 * s^-2

A_field = (vacuum_permittivity / (4 * np.pi)) * (   (3*(m.dot(m)))/((R.x**2 + R.y**2 + R.z**2)**(5/2)) - m/((R.x**2 + R.y**2 + R.z**2)**(3/2))  )
delop = Del()
B_field = delop.cross(A_field)

param_circle = ParametricRegion((4*cos(theta), 4*sin(theta)), (theta, 0, 2*pi))
param_parabolic_surface = ImplicitRegion((x, y, z), Eq(z, x**2 + y**2))

print(B_field)
print(B_field.doit())

print(is_conservative(B_field))

vector_integrate(1, param_circle)

print()
print(vector_integrate(B_field, param_circle))
print("...")

#print(vector_integrate(B_field, param_parabolic_surface))
#print("Finished.")






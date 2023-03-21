import sympy
from sympy import symbols, integrate, limit, cos, sin, exp
x = symbols('x')


y = (5*x**2 + 2*x - 1)/x**0.5

y_diff = y.diff(x)
y_integral = integrate(y,x)
y_limit = limit(y, x, 0)
print("f(x) = {}".format(y))

print("f'(x) = {}".format(y_diff))

print("∫f(x)dx = {}".format(y_integral))

print("limf(x) x -> 0 = {}".format(y_limit))

y2 = (2 + cos(x))/(sin(x))**2
y_diff_2 = y2.diff(x)
y_integral_2 = integrate(y2,x)
y_limit_2 = limit(y2, x, 0)

print()

print("f(x) = {}".format(y2))

print("f'(x) = {}".format(y_diff_2))

print("∫f(x)dx = {}".format(y_integral_2))

print("limf(x) x -> 0 = {}".format(y_limit_2))

y3 = x**3 * exp(-4*x)
y_diff_3 = y3.diff(x)
y_integral_3 = integrate(y3,x)
y_limit_3 = limit(y3, x, 0)

print()

print("f(x) = {}".format(y3))

print("f'(x) = {}".format(y_diff_3))

print("∫f(x)dx = {}".format(y_integral_3))

print("limf(x) x -> 0 = {}".format(y_limit_3))
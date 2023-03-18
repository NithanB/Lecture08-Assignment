import sympy
from sympy import symbols, integrate, limit
x = symbols('x')


y = (5*x**2 + 2*x - 1)/x**0.5

y_diff = y.diff(x)
y_integral = integrate(y,x)
y_limit = limit(y, x, 0)
print("f(x) = {}".format(y))

print("f'(x) = {}".format(y_diff))

print("∫f(x)dx = {}".format(y_integral))

print("limf(x) x -> 0 = {}".format(y_limit))


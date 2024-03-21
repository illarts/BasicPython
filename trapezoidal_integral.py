from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

def trapezoidal_integral(f, a = 0, b = 1, n = 100):
    k = 1
    h = (b - a) / n
    s = 0
    
    while k <= n:
        s += (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))
        
        k = k + 1
        
    return s

def q1(x):
    return sin(x)

def q2(x):
    return 4 / (1 + x**2)
    
def q3(x):
    return math.pi**(1/2) * (math.exp(-x**2))

q1 = trapezoidal_integral(q1, 0, math.pi * 1 / 2, 50)
q2 = trapezoidal_integral(q2, 0, 1, 100)
q3 = trapezoidal_integral(q3, -100, 100, 100)

print(q1)
print(q2)
print(q3)
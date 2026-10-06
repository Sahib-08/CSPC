"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0


x = 0
lr = 0.1
small = 0.001

while True:
  x_next = x - lr*df(x)
  if abs(x - x_next) < small:
    x = x_next
    break
  x = x_next
print("2A By hand, f(x) =", f(x), "x =", x)

newton_x = newton(df, 0, fprime=d2f)
print("2A Newton method, f(x) =", f(newton_x), "x =", newton_x)

slsqp_x = minimize(f, 0, method="SLSQP")
print("2A SLSQP, f(x) =", slsqp_x.fun, "x =", slsqp_x.x[0])



    

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

x = 0

while True:
  x_next = x - lr*dg(x)
  if abs(x - x_next) < small:
    x = x_next
    break
  x = x_next
print("2B from 0 By hand, g(x) =", g(x), "x =", x)

newton_x = newton(dg, 0, fprime=d2g)
print("2B from 0 Newton method, g(x) =", g(newton_x), "x =", newton_x, "d2g(x) =", d2g(newton_x))

slsqp_x = minimize(g, 0, method="SLSQP")
print("2B from 0 SLSQP, g(x) =", slsqp_x.fun, "x =", slsqp_x.x[0])

x = 2

while True:
  x_next = x - lr*dg(x)
  if abs(x - x_next) < small:
    x = x_next
    break
  x = x_next
print("2B from 2 By hand, g(x) =", g(x), "x =", x)

newton_x = newton(dg, 2, fprime=d2g)
print("2B from 2 Newton method, g(x) =", g(newton_x), "x =", newton_x, "d2g(x) =", d2g(newton_x))

slsqp_x = minimize(g, 2, method="SLSQP")
print("2B from 2 SLSQP, g(x) =", slsqp_x.fun, "x =", slsqp_x.x[0])
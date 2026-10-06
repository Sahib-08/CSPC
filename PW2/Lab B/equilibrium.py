"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0


def k_imbalance(x):
    return (2 * x) ** 2 / ((a - x) * (b - x)) - K


x_newton = newton(k_imbalance, x0=0.5)

def objective(x):
    return k_imbalance(x[0]) ** 2

result = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)]
)

print("Equilibrium extent:")
print("  Newton method: x =", x_newton)
print("  Minimization: x =", result.x[0])

print("H2 =", 1 - x_newton, "mol")
print("I2 =", 1 - x_newton, "mol")
print("HI =", 2 * x_newton, "mol")

x = np.linspace(0, 0.999, 100)
plt.plot(x, 1 - x, label="H2")
plt.plot(x, 1 - x, label="I2")
plt.plot(x, 2 * x, label="HI")
plt.axvline(x_newton, linestyle="--", color="black")
plt.xlabel("Extent x")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")
plt.show()
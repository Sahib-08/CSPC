"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


t, C = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1, unpack=True)
C0 = C[0]

def total_error(k):
    return np.sum((C - C0*np.exp(-k * t)) ** 2)


result = minimize(total_error, method="SLSQP", bounds=[(0, 5)], x0=0.5)
print("Fitted k:", result.x[0])

t_fit = np.linspace(t.min(), t.max(), 200)
C_fit = C0 * np.exp(-result.x[0] * t_fit)
plt.scatter(t, C, label="Measured data")
plt.plot(t_fit, C_fit, label="Fitted curve")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.tight_layout()
plt.savefig("kinetics.png")
plt.show()
"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)


v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))

plt.plot(t, y, 'o-')
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Position over Time")
plt.show()

plt.plot(t, v, 'o-')
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Velocity over Time")
plt.show()

plt.plot(t, a, 'o-')
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.title("Acceleration over Time")
plt.show()


integral_v = cumulative_trapezoid(a, t, initial=0) + v[0]
integral_y = cumulative_trapezoid(integral_v, t, initial=0) + y[0]

plt.plot(t, integral_v, 'o-')
plt.xlabel("Time")
plt.ylabel("Integrated Velocity")
plt.title("Integrated Velocity over Time")
plt.show()

plt.plot(t, integral_y, 'o-')
plt.xlabel("Time")
plt.ylabel("Integrated Position")
plt.title("Integrated Position over Time")
plt.show()


fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, color="red", linestyle="--", label="True g = -9.81 m/s²")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png")
plt.show()

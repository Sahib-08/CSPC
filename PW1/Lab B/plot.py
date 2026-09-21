"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

LAMBDA = 0.3     # decay constant, given

file = sys.argv[1]
output = sys.argv[2]

t = []
observed = []

with open(file) as f:
    reader = csv.DictReader(f)

    for row in reader:
        t.append(float(row["time"]))
        observed.append(int(row["count"]))

N0 = observed[0]

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(8, 4))

ax1.scatter(t, observed, color='blue')
ax1.set_title('Observed data')

t_vals = np.array(t)
analytical = N0 * np.exp(-LAMBDA * t_vals)
ax2.plot(t_vals, analytical, color='red', marker='o')  
ax2.set_title('Analytical')

fig.supxlabel("Time")
fig.supylabel("Atoms")

plt.tight_layout()
plt.savefig(output)
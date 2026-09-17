"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # simulate function rejects negative lam
    with pytest.raises(ValueError):
        simulate(1000, -0.2)


def test_matches_law():
    # test if the simulation matches the law N0*exp(-lam*t)
    seeds = 10000
    n = 1000
    lam = 0.3
    t = 16

    simulations = [
        simulate(n, lam, seed=i)
        for i in range(seeds)
    ]

    times = []

    for i in simulations:
        times.append(i[t])

    assert sum(times) / seeds == pytest.approx(n * np.exp(-lam * t * 0.05), rel=0.02)
    # multiply -lam*t by dt(0.05)


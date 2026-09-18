from decay import simulate, simulate_loop
import time
import numpy as np # simulate function needs numpy, not sure if I need to import it in this file also, did it just in case

start = time.perf_counter()

for i in range(100):
    simulate(10000, 0.1, seed = i)

end = time.perf_counter()

fast = end - start


start = time.perf_counter()

for i in range(100):
    simulate_loop(10000, 0.1, seed = i)

end = time.perf_counter()

slow = end - start

print("Loop version: " + str(slow) + " seconds")
print("Numpy version: " + str(fast) + " seconds")
print("The fast vectorized version is " + str(slow / fast) + " times faster than the slow, loop based version.")
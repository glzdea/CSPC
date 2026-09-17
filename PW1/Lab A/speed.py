import time
from decay import simulate_loop, simulate

N0 = 10000
lam = 0.4
runs = 5

# Time pure Python loop
start = time.perf_counter()
for i in range(runs):
    simulate_loop(N0, lam, seed=i)
loop_time = (time.perf_counter() - start) / runs

# Time NumPy version
start = time.perf_counter()
for i in range(runs):
    simulate(N0, lam, seed=i)
numpy_time = (time.perf_counter() - start) / runs

print(f"loop : {loop_time:.6f} s")
print(f"numpy: {numpy_time:.6f} s")
print(f"speed-up: {loop_time / numpy_time:.2f} x")
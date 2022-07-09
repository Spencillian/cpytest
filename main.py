import cytest
import time
import mixcypy


def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


start_py = time.perf_counter()
pyprimes = primes(10000000)
time_py = time.perf_counter() - start_py

print(f"Python: {time_py} seconds")


start_cy = time.perf_counter()
cyprimes = cytest.primes(10000000)
time_cy = time.perf_counter() - start_cy

print(f"Cython: {time_cy} seconds")


start_mix = time.perf_counter()
mixprimes = mixcypy.primes(10000000)
time_mix = time.perf_counter() - start_mix


print(f"Mixcypy: {time_mix} seconds")

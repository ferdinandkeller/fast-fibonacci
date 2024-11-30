import gmpy2
from loguru import logger
import time

# we need to go into the hundreds of millions to see a difference
n = 200_000_000

start_time = time.time()
gmpy2.fib(n)
gmpy_time = time.time() - start_time
logger.info(f"Time taken by gmpy2.fib: {gmpy_time} seconds")


def fib_fast_doubling(n: int):
    """
    Compute the nth Fibonacci number using the fast doubling method.

    :param n: The index of the Fibonacci number to compute.
    :return: The nth Fibonacci number.
    """

    def _fib(n):
        if n == 0:
            return (gmpy2.mpz(0), gmpy2.mpz(1))
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    result, _ = _fib(n)
    return result


start_time = time.time()
fib_fast_doubling(n)
fast_doubling_time = time.time() - start_time
logger.info(f"Time taken by fib_fast_doubling: {fast_doubling_time} seconds")

logger.info(f"Fast doubling in Python is {fast_doubling_time / gmpy_time}x slower.")

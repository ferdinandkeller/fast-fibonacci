# Fast Fibonacci Comparison

This project aims to compare the performance of the `gmpy2` library's Fibonacci function with a Python implementation using the fast doubling method. The goal is to demonstrate that the Python implementation is impressively close in performance to the highly optimized `gmpy2` library, even for very large Fibonacci numbers.

## Overview

The code calculates the 200,000,000th Fibonacci number using both methods and measures the time taken for each. The results show that the Python implementation is barely 2x slower than the `gmpy2` implementation, which is quite impressive given the expectations of a much larger difference.

## Python Implementation Details

While the logic of the fast doubling method is implemented in Python, we use GMP big integers to handle the large numbers involved. This allows us to leverage the efficiency of GMP for arithmetic operations while keeping the algorithm itself in Python.

## Why Such a Large Number?

To ensure that the calculations take a significant amount of time and provide a meaningful comparison, we use a very large Fibonacci number (200,000,000). This allows us to observe the performance characteristics of both methods more clearly.

## Fun Fact

The 200,000,000th Fibonacci number is approximately 40MiB in size! You can find this massive number in the `fib_200_000_000.txt` file if you're curious to see it.

## Running the Code

The easiest way to run the code is to have `uv` installed. To see the performance comparison for yourself, simply execute the `fib.py` script. Make sure you have the required dependencies installed.

```bash
uv sync
uv run fib.py
```

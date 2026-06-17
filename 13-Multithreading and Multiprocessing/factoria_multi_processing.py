'''
Real_world Example-Multiprocessing for CPU-bound tasks
Scernario:Factorial Calculation
Factorial Calcualtion , especially for large numbers, involves significant computational work. Multiprocessing can help speed up the calculation by distributing the workload across multiple CPU cores.
'''

import multiprocessing
import time
import sys
import math

###Increasse the maximum number of digits for interger conversion
sys.set_int_max_str_digits(100000)

### function

def factorial(n):
    print(f"Calculating factorial of {n}")
    result=math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers=[5000,6000,7000]

    start_time=time.time()
  ### Create a pool of worker processes
    with multiprocessing.Pool(processes=4) as pool:
        results=pool.map(factorial, numbers)

    end_time=time.time()
    print(f"Time taken: {end_time-start_time} seconds")

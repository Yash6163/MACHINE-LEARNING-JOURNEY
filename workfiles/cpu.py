import multiprocessing
import math
import sys
import time
#increase no of digits for integer
sys.set_int_max_str_digits(1000000)

#function to compute factorial
def compute_factorial(number):
    print(f"factorial of {number}")
    result=math.factorial(number)
    return result

if __name__== "__main__" :
    numbers=[5000,6000,7000,8000]
    start_time=time.time()
     #crreate a pool of worker processes
    with multiprocessing.Pool() as pool :
        results=pool.map(compute_factorial,numbers)

    end=time.time()
    print(f"RESULTS : {results}")
    print(f"TIME TAKEN  : {end-start_time}")
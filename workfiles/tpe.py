##multiprocessing thread pool execution
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"NUMBER : {number}"

numbers=[1,2,3,4,5]

##are yhn kya hua age m simple pass marta na to list jati pr using thread vo intrger process kr lera
## aur execution time 5 ki jgh 2 hogya 

with ThreadPoolExecutor(max_workers=3)as executor :
    results=executor.map(print_numbers,numbers)

for result in results :
    print (f"RESULT IS : {result}")
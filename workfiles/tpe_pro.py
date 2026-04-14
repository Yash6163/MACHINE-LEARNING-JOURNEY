##multiprocessing thread pool execution
from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"NUMBER : {number*number}"

if __name__=="__main__":
    numbers=[1,2,3,4,5]

    ##are yhn kya hua age m simple pass marta na to list jati pr using thread vo intrger process kr lera
    ## aur execution time 5 ki jgh 2 hogya 

    with ProcessPoolExecutor(max_workers=2)as executor :
        results=executor.map(square_numbers,numbers)

    for result in results :
        print (f"RESULT IS : {result}")
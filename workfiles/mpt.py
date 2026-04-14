##multi threading
#when ot use multithreading
## i/o bound task

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"NUMBER : {i}")

def print_letter():
    for letter in 'ABCDE':
        time.sleep(2)
        print(f"LETTER : {letter}")

if __name__ =="__main__" :
    ##create two threads
    t1=multiprocessing.Process(target=print_numbers)
    t2=multiprocessing.Process(target=print_letter)
        
    t=time.time()
    t1.start()
    t2.start()
    ##to wait for threads to complete 
    t1.join()
    t2.join()

    finished_time=time.time()-t
    print(finished_time)
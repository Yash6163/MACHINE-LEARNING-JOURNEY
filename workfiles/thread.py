##multi threading
#when ot use multithreading
## i/o bound task

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"NUMBER : {i}")

def print_letter():
    for letter in 'ABCDE':
        time.sleep(2)
        print(f"LETTER : {letter}")

##create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)
    
t=time.time()
t1.start()
t2.start()
##to wait for threads to complete 
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)
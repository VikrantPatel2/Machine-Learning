 ### Multithreading in Python
## Multithreading allows you to run multiple threads (lightweight processes) concurrently within a single program. This can be useful for tasks that involve waiting for I/O operations, such as reading from a file or making network requests, as it allows other threads to continue executing while one thread is waiting. 

### Concurrent excuetion: When you want to improve the throughput of application by performing multiple operation simultaneously, you can use multithreading. It allows you to run multiple threads of execution concurrently, which can help improve the performance of your application by allowing it to perform multiple tasks at the same time.

import threading
import time 


def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcdef":
        time.sleep(2)
        print(f'Letter: {letter}')

### Create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()

### start the threads
t1.start()
t2.start()

### wait for the threads to complete
t1.join()
t2.join()
finish=time.time()-t
print(f'Time taken: {finish} seconds')
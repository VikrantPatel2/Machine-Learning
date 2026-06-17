## Process that run in parallel
### CPU_Bound Tasks-Tasks that are  heavy on CPU usage
### Parallel excuetion: Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(1,6):
        time.sleep(1)
        print(f'Square of {i} is {i**2}')


def cube_numbers():
    for i in range(1,6):
        time.sleep(1.5)
        print(f'Cube of {i} is {i**3}')        

if __name__ == "__main__":

            ## Create 2 processes
            p1=multiprocessing.Process(target=square_numbers)
            p2=multiprocessing.Process(target=cube_numbers)
            t=time.time()
            ### start the processes
            p1.start()
            p2.start()

            ### Wait for the processes to complete
            p1.join()
            p2.join()

            finished=time.time()-t
            print(f'Time taken: {finished} seconds')
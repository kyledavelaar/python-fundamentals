from time import sleep, perf_counter
from threading import Thread
import concurrent.futures

# Threads good for I/O tasks: connecting to DB, network requests
# Threads hold a lock and only 1 thread can hold the lock at a single time
# so best used on async tasks that only hold onto the lock for a very short time and then release it (like i/o tasks)

# Processes good for computation: video compression/streaming, prime number finder, etc.


def run_threads():
    print("============== THREAD ==============")
    def task(x):
        print('starting task: {}'.format(x))
        sleep(1)
        print('done')


    start_time = perf_counter()

    task(1)
    task(2)

    end_time = perf_counter()

    print(f'it took {end_time - start_time} to complete 2 tasks on a single thread')

    start_time2 = perf_counter()

    thread1 = Thread(target=task, args=(1,))
    thread2 = Thread(target=task, args=(2,))

    thread1.start()
    thread2.start()

    # wait for threads to finish
    thread1.join()
    thread2.join()

    end_time2 = perf_counter()

    print(f'it took {end_time2 - start_time2} to finish 2 tasks on 2 threads')

################################################################################################################
## multi-process
################################################################################################################


def process_task(x):
    """
    For multi-processing the task function must be in global state (cannot live inside run_processes())
    """
    sleep(1)
    return x*x

def run_processes():
    print('*********** MULTI PROCESS ******************')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(process_task, [1,2,3,4,5]))

    for result in results:
        print(result)


if __name__ == '__main__':
    # run_processes()
    run_threads()


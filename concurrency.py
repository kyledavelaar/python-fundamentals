from time import sleep, perf_counter
from threading import Thread

# Threads good for I/0 tasks: connecting to DB, network requests
# Processes good for computation: video compression/streaming, prime number finder, etc.


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

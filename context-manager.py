# context managers are useful for automatically running enter and exit hooks before any function.
# this allows for initializing and cleanup logic to automatically run whenever the context manager is used

class MyContextManager:
    def __enter__(self):
        # initialize things
        print(f'entering the context manager')
        return self # must always return self from __enter__

    def __exit__(self, exc_type, exc_val, exc_tb):
        # cleanup logic
        print(f'exiting the context manager')

    def run(self, words: str):
        print(f'running something on myContextManager: {words}')

with MyContextManager() as mcm:
    mcm.run('it was the beginning')


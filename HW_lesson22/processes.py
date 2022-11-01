import random
import time
import pandas as pd
import multiprocessing

print(multiprocessing.cpu_count())
results = {}
results['workers'] = []
results['elapsed time'] = []


class Timer:
    def __init__(self):
        self.start = 0
        self.finish = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish = time.time()
        result = self.finish - self.start
        results['elapsed time'].append(result)

timer = Timer()


DATA_SIZE = 1_000_000
lst = []


def fill_data(n):
    name = multiprocessing.current_process().name
    print(name)
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


def get_data(workers):
    results['workers'].append(workers)
    with timer:
        jobs = []
        for i in range(workers):
            process = multiprocessing.Process(
                target=fill_data,
                args=(DATA_SIZE//workers,)
            )
            jobs.append(process)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()
        # with multiprocessing.Pool(workers) as processes:
        #     pool = processes.map(fill_data, [DATA_SIZE//workers for _ in range(workers)])


if __name__ == '__main__':
    for workers in range(1, 20):
        get_data(workers)
    df = pd.DataFrame(data=results)
    with open("multiprocessing_result.csv", "w") as file:
        file.write(df.to_csv(index=False))
    print(df)

import os
import time
import pandas as pd
import requests
import string
import threading
import random


def time_decor(func):
    def wrapper(streams, pic):
        start = time.time()
        func(streams, pic)
        finish = time.time()
        result = finish - start
        return result
    return wrapper


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/400'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


@time_decor
def get_streams(streams, pic):
    threads = [threading.Thread(target=fetch_pic, args=(pic//streams,)) for _ in range(streams)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

results = {}


def get_db(num_pic, period):
    results['threads'] = []
    for j in range(period, num_pic+period, period):
        results[f'{j} pictures'] = []
        for i in range(2, 14, 2):
            results[f'{j} pictures'].append(get_streams(i, j))
            if f'threads {i}' not in results['threads']:
                results['threads'].append(f'threads {i}')


if __name__ == '__main__':
    get_db(500, 100)
    df = pd.DataFrame(data=results)
    with open("multithreading_result.csv", "w") as file:
        file.write(df.to_csv(index=False))
    print(df)



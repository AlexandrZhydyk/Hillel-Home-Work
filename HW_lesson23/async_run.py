"""Asynchronous download"""
import asyncio
import os
import random
import time

import aiohttp


async def use_future_result(my_future):
    future = await my_future
    print(f"Future received {future}")


async def pic_download(url, session):

    async with session.get(url, allow_redirects=True) as response:
        path = os.path.join(os.getcwd(), 'image')
        data = await response.read()
        name = random.randint(1, 1000000000)
        with open(f'{path}/{name}.jpg', 'wb') as f:
            f.write(data)

url = 'https://picsum.photos/400/400'


async def get_aihttp_session(my_future):
    async with aiohttp.ClientSession() as session:
        task_list = []
        for i in range(10):
            task = pic_download(url, session)
            task_list.append(task)
        await asyncio.gather(*task_list)
        print("Pictures downloaded")
        my_future.set_result('Done!')


async def main():
    future = asyncio.Future()
    await asyncio.gather(
        get_aihttp_session(future),
        use_future_result(future),
    )


if __name__ == "__main__":
    time_start = time.time()
    asyncio.run(main())
    print(time.time()-time_start)

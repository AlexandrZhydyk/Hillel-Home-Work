import aiohttp
import asyncio
import os
import random


async def pic_download(url, session):

    async with session.get(url, allow_redirects=True) as response:
        path = os.path.join(os.getcwd(), 'image')
        data = await response.read()
        name = random.randint(1, 1000000000)
        with open(f'{path}/{name}.jpg', 'wb') as f:
            f.write(data)

url = 'https://picsum.photos/400/400'


async def get_aihttp_session():
    async with aiohttp.ClientSession() as session:
        task_list = []
        for i in range(10):
            task = pic_download(url, session)
            task_list.append(task)
        await asyncio.gather(*task_list)


async def use_future_result(my_future, event_loop):
    future = await my_future
    print(f"Future received {future}")
    event_loop.stop()


async def get_future_result(my_future):
    await asyncio.sleep(1)
    my_future.set_result("Done")


event_loop = asyncio.new_event_loop()
future = asyncio.Future(loop=event_loop)
event_loop.create_task(get_aihttp_session())
event_loop.create_task(use_future_result(future, event_loop))
event_loop.create_task(get_future_result(future))

event_loop.run_forever()
event_loop.close()

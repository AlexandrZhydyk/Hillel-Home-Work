"""Simple example"""
import asyncio


async def worker():
    while True:
        await asyncio.sleep(1)
        print('worker1')


async def worker1():
    while True:
        await asyncio.sleep(2)
        print('worker2')


async def worker2():
    while True:
        await asyncio.sleep(3)
        print('worker3')


async def main():
    await asyncio.gather(
        worker(),
        worker1(),
        worker2(),
    )

asyncio.run(main())

import asyncio
import time

async def async_sleep(s: int):
    asyncio.sleep(s)

async def sleep_for_s(s: int) -> str:
    await async_sleep(s)
    return f"Slept for {s} seconds."

async def runner():
    tasks = [asyncio.create_task(sleep_for_s(i)) for i in range(1, 3)]
    for task in asyncio.as_completed(tasks):
        reader = await task
        print(reader)


asyncio.run(runner())
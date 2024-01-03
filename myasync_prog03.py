#!/usr/bin/env python3

import asyncio

# define our function with "async def"
async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)
    print(f'{n} Goodbye!')

async def main():
    t1 = asyncio.create_task(hello(1))
    t2 = asyncio.create_task(hello(2))
    t3 = asyncio.create_task(hello(3))

    await t1
    await t2
    await t3


# run the async def, and get a coroutine back
# schedule the coroutine with asyncio.run
asyncio.run(main())
print('Done')

#!/usr/bin/env python3

import asyncio

# define our function with "async def"
async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)
    print(f'{n} Goodbye!')

async def main():
    for i in range(5):
        await hello(i)

# run the async def, and get a coroutine back
# schedule the coroutine with asyncio.run
asyncio.run(main())
print('Done')

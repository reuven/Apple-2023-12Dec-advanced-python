#!/usr/bin/env python3

import asyncio

# define our function with "async def"
async def hello(n):
    print(f'{n} Hello!')

# run the async def, and get a coroutine back
# schedule the coroutine with asyncio.run

asyncio.run(hello(5))

#!/usr/bin/env python3

import asyncio

# define our function with "async def"
async def hello(n):
    print(f'{n} Hello!')

async def main():
    for i in range(5):
        hello(i)
    

# run the async def, and get a coroutine back
# schedule the coroutine with asyncio.run
for i in range(5):
    asyncio.run(hello(i))

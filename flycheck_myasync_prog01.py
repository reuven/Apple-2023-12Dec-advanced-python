#!/usr/bin/env python3

import asyncio

# define our function with "async def"

async def hello(n):
    print(f'{n} Hello!')

asyncio.run(hello(5))
import asyncio


async def cor1(s: int):
    await asyncio.sleep(s)
    print("cor1")
    return "cor1"

async def cor2(s: int):
    await asyncio.sleep(s)
    print("cor2")
    return "cor2"


# tsk1 = asyncio.create_task(coro=cor1(5))
# tsk2 = asyncio.create_task(coro=cor2(7))
async def main():
    # result = await asyncio.gather(cor1(5), cor2(3))
    # print(result)
    tsk1 = asyncio.create_task(coro=cor1(5))
    tsk2 = asyncio.create_task(coro=cor2(3))
    await tsk1
    await tsk2

asyncio.run(main=main())

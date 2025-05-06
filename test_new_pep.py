import asyncio

def f(*args):
    return args

async def gen():
    for i in range(5):
        await asyncio.sleep(0.001)
        yield i




assert [1 for _ in range(2)] == [1, 1]
assert [(1, 2) for _ in range(2)] == [(1, 2), (1, 2)]
assert [*(1, 2), *(1, 2)] == [1, 2, 1, 2]
assert [*(1, 2) for _ in range(2)] == [1, 2, 1, 2]

assert {1 for _ in range(2)} == {1}
assert {(1, 2) for _ in range(2)} == {(1, 2)}
assert {*(1, 2), *(1, 2)} == {1, 2}
assert {*(1, 2) for _ in range(2)} == {1, 2}


assert list((1 for _ in range(2))) == [1, 1]
assert list(((1, 2) for _ in range(2))) == [(1, 2), (1, 2)]
assert list(iter([(1, 2), (1, 2)])) == [(1, 2), (1, 2)]
assert list((*(1, 2) for _ in range(2))) == [1, 2, 1, 2]

assert f(1, 2) == (1, 2)
assert f(*(1, 2)) == (1, 2)
assert f(*(1, 2), *(1, 2)) == (1, 2, 1, 2)
assert f(*(1 for _ in range(2))) == (1, 1)
assert f(*((1, 2) for _ in range(2))) == ((1, 2), (1, 2))
assert f(*(1 for _ in range(2))) == (1, 1)
assert f(*((1, 2) for _ in range(2))) == ((1, 2), (1, 2))
it = (*(1, 2) for _ in range(2))
assert f(*it) == (1, 2, 1, 2)
assert f(*(*(1, 2) for _ in range(2))) == (1, 2, 1, 2)
assert f(*((1, 2) for _ in range(2))) == ((1, 2), (1, 2))
assert f(*(1, 2) for _ in range(2)) != ((1, 2), (1, 2))




async def main_L():
    print([*(1, 3) async for x in gen()])

async def main_S():
    print({*(1, 3) async for x in gen()})

async def main_G():
    squares = (*(1, 3) async for x in gen())
    async for x in squares:
        print(x)

asyncio.run(main_L())
asyncio.run(main_S())
#asyncio.run(main_G())


"""
assert {1: 2 for _ in range(2)} == {1: 2}
a = {1: 2}
b = {1: 3}
assert {**a, **b} == {1: 3}
assert {**d for d in [a, b]} == {1: 3}
"""


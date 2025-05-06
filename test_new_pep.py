import asyncio

def f(*args):
    return args




import dis

try:
    dis.dis('f"{*1}"')
except SyntaxError:
    pass
else:
    print("Fstring did not raise")


assert [1 for _ in range(2)] == [1, 1]
assert [(1, 2) for _ in range(2)] == [(1, 2), (1, 2)]
assert [*(1, 2), *(1, 2)] == [1, 2, 1, 2]
assert [*(1, 2) for _ in range(2)] == [1, 2, 1, 2]

assert {1 for _ in range(2)} == {1}
assert {(1, 2) for _ in range(2)} == {(1, 2)}
assert {*(1, 2), *(1, 2)} == {1, 2}
assert {*(1, 2) for _ in range(2)} == {1, 2}
# Also works with walrus operator
assert [*(a:=[1, 3]) for i in range(2)] == [1, 3, 1, 3]

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

assert {1: 2 for _ in range(2)} == {1: 2}
a = {1: 2}
b = {1: 3}
c = {2: 5}
assert {**a, **b} == {1: 3}
assert {**d for d in [a, b]} == {1: 3}
assert {**d for d in [a, b, c]} == {1: 3, 2: 5}






async def gen():
    for i in range(5):
        await asyncio.sleep(0.001)
        yield i


async def gen2():
    for i in range(5):
        await asyncio.sleep(0.001)
        yield i, i

async def gen3():
    for i in range(5):
        await asyncio.sleep(0.001)
        yield {i: i}


async def main_L():
    print([*(1, 3) async for x in gen()])

async def main_S():
    print({*(1, 3) async for x in gen()})

async def main_D():
    print({**d async for d in gen3()})

async def main_G():
    squares = (*(1, 3) async for x in gen())
    async for x in squares:
        print(x)

async def main_G2():
    async for _v in (*x async for x in gen2()):
        print(_v)


asyncio.run(main_L())
asyncio.run(main_S())
asyncio.run(main_D())
asyncio.run(main_G())
#asyncio.run(main_G2())



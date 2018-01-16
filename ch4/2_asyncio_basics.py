import asyncio


def function_1(end_time, loop):
    print('Function 1 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()


def function_2(end_time, loop):
    print('Function 2 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()


def function_3(end_time, loop):
    print('Function 3 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()


if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    end_loop = async_loop.time() + 9.0

    async_loop.call_soon(function_1, end_loop, async_loop)

    async_loop.run_forever()
    async_loop.close()

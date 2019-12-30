"""
协程说明：
    1. 语法上，协程和生成器类似，都是包含 yield 关键字的函数。但是：
        a. 在协程中， yield 通常出现在表达式的右边，可以产出值，也可以不产出（产出 None）
        b. 协程可能会从调用方接收数据，使用的是 send 函数。生成器配套使用的是 next 函数。
    2. 从根本上把 yield 视作控制流程的方式。
    3. 调用函数得到生成器对象。见例子 1
    4. 可以调用 next(my_coro) 或者 my_coro.send(None) 激活/预激协程（即，让协程向前执行到第一个 yield 表达式）。
    5. 协程中 return 表达式的值会传给调用方，赋值给 StopIteration 异常的一个属性。
"""


# 例子 1
def co1():
    print('coroutine started')
    x = yield
    print('received x = ', x)

my_coro1 = co1()        # 得到生成器对象
print(next(my_coro1))   # 启动生成器
print(my_coro1.send(42))    # yield 表达式计算出 42，协程恢复，一直运行到下一个 yield 表达式，或者终止抛出 StopIteration 异常。
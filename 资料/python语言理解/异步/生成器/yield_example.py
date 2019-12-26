"""
生成器：
    生成器不会把结果保存在一个系列中，而是保存生成器的状态，在每次进行迭代时返回一个值，直到遇到 StopIteration 异常结束。

生成器种类：
    1. 生成器表达式
        同列表解析语法，只是把 [] 换成 ()
        例：gen = (x**2 for x in range(5))
    2. 生成器函数
        包含 yield 关键字的函数

生成器知识点：
    1. 生成器是迭代器，见例子 1
    2. 在函数生成器中，如果没有 return ，则默认执行到函数完毕时返回 StopIteration，见例子 2
        如果有 return ，则在碰到 return 的时候直接抛出异常，异常值就是 return 的值，见例子 3
    3. 生成器支持的方法：
        a. close() 手动关闭生成器函数，后面的调用会直接返回 StopIteration 异常，见例子 4
        b. send() 接受外部传入的一个变量，见例子 5
        c. throw() 用来向生成器函数送入一个异常，可以是系统定义的异常，也可以是自定义的异常。
            生成器函数有三种行为：
            1. 直接抛出这个异常（没有处理异常或者处理异常的行为就是原样抛出），结束函数。见例子 6
            2. 消化了异常，然后运行到下一个 yield。见例子 7
            3. 消化了异常，但是没有下一个 yield ，直接运行到程序的结尾（生成器的行为，这个时候会抛出 StopIteration 异常）。见例子 8
"""

# ----------------------------例子 1----------------------------
def ex1_1():
    gen = (x ** 2 for x in range(1, 4))
    for i in gen:
        print('> %d' % i)


def ex1_2():
    n = 3
    val = 2
    while n:
        yield val
        val **= 2
        n -= 1


print('例子1开始：')
ex1_1()         # 表达式生成器当作迭代器使用例子
print('')

g1_1 = ex1_2()  # 函数生成器当作迭代器使用例子
for i in g1_1:
    print('> %d' % i)
print('例子1结束。\n')


# ----------------------------例子 2----------------------------
def ex2_1():
    yield 1
    yield 2


print('例子2开始：')
g2_1 = ex2_1()
try:
    print(next(g2_1))
    print(next(g2_1))
    print(next(g2_1))      # 程序试图从yield语句的下一条语句开始执行，发现已经到了结尾，所以抛出StopIteration异常。
except StopIteration:
    print('收到 StopIteration')
print('例子2结束。\n')


# ----------------------------例子 3----------------------------
def ex3_1():
    yield 1
    yield 2
    return 'abcdefg'


print('例子3开始：')
g3_1 = ex3_1()
try:
    print(next(g3_1))
    print(next(g3_1))
    print(next(g3_1))      # 程序试图从yield语句的下一条语句开始执行，发现已经到了结尾，所以抛出StopIteration异常。
except StopIteration as e:
    print('收到 StopIteration，值: ' + str(e.value))
print('例子3结束。\n')


# ----------------------------例子 4----------------------------
def ex4_1():
    yield 1
    yield 2
    return 'abcdefg'


print('例子4开始：')
g4_1 = ex4_1()
try:
    print(next(g4_1))
    g4_1.close()
    print(next(g4_1))       # 关闭后无法再获取值
except StopIteration as e:
    print('收到 StopIteration，值: ' + str(e.value))
print('例子4结束。\n')


# ----------------------------例子 5----------------------------
def gen5_1():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'get %s' % receive


try:
    print('例子5开始：')
    g5_1 = gen5_1()
    """
    g5_1.send(None) 或者 next(g5_1) 可以启动生成器函数，并执行到第一个 yield 语句结束的位置。
    此时，执行完 yield value 语句返回 value 的值（0）给外部，但是并没有给 receive 赋值。
    """
    print(g5_1.send(None))
    """
    通过 g5_1.send('hello') ，传入 'hello' 并赋值给 receive ，然后计算新的 value 的值，返回 while 头部，执行到 yield value 再次停止，
    并返回 get hello ，然后挂起自己。
    """
    print(g5_1.send('hello'))
    """
    同上
    """
    print(g5_1.send(123))
    """
    执行 break 退出循环，最后整个函数执行完毕，抛出 StopIteration 异常。
    """
    print(g5_1.send('e'))
except StopIteration as e:
    print('收到 StopIteration，值：' + str(e.value))
print('例子5结束。\n')


# ----------------------------例子 6----------------------------
def gen6_1():
    yield 1
    yield 2
    yield 3
    yield 4

try:
    print('例子6开始：')
    g6_1 = gen6_1()
    print(next(g6_1))
    print(g6_1.throw(TypeError, 'Oh no!'))
    print(next(g6_1))       # 我不会产生作用了
except Exception as e:
    print('异常: ' + str(e))
print('例子6结束。\n')


# ----------------------------例子 7----------------------------
def gen7_1():
    i = 0
    while True:
        try:
            yield i
            i += 1
        except TypeError as e:
            print('内部处理异常[{exc}]，OK!'.format(exc = str(e)))


try:
    print('例子7开始：')
    g7_1 = gen7_1()
    print(next(g7_1))
    print('attention: ' + str(g7_1.throw(TypeError, 'Oh no!')))  # 这里输出 0 是因为接到异常直接跳到异常处理的代码，然后重新执行 while 内部逻辑。
    print(next(g7_1))
except Exception as e:
    print('异常: ' + str(e))
print('例子7结束。\n')


# ----------------------------例子 8----------------------------
def gen8_1():
    i = 0
    while True:
        try:
            yield i
            i += 1
        except TypeError as e:
            print('内部处理异常[{exc}]，OK!'.format(exc = str(e)))
        except ValueError as e:
            break
    print('我要结束了')


try:
    print('例子8开始：')
    g8_1 = gen8_1()
    print(next(g8_1))
    print('attention: ' + str(g8_1.throw(TypeError, 'Oh no!')))  # 这里输出 0 是因为接到异常直接跳到异常处理的代码，然后重新执行 while 内部逻辑。
    print(next(g8_1))
    print(g8_1.throw(ValueError, 'hahahahaha!'))
    print(next(g8_1))
except Exception as e:
    print('收到 StopIteration 异常: ' + str(type(e)))
print('例子8结束。\n')
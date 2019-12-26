# 2. 例子
"""
调用方：调用委派生成器的客户端（调用方）代码
委托生成器：包含 yield from 表达式的生成器函数。作用是在调用方和子生成器之间建立一个双向通道。
子生成器：yield from 后面加的生成器函数

双向通道的意思是：调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。
"""

# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total / count


# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)      # 预激生成器
    print(calc_average.send(10))    # 打印 10.0
    print(calc_average.send(20))    # 打印 20.0
    print(calc_average.send(30))    # 打印 30.0


if __name__ == "__main__":
    main()
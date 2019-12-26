"""
yield from 作用：
1. yield from 后面加可迭代对象，可以把可迭代对象里面的每个元素一个个 yield 出来，使得代码
    更加简洁，逻辑更清晰。见 yield_from_example1.py 的例子 1
2. yield from 后面加上一个生成器后，可以实现生成的嵌套。见 yield_from_example1.py 的例子 2
"""

# 例子 1
def gen_with_yield(*arg, **kw):
    for items in arg:
        for item in items:
            yield item


def gen_with_yield_from(*arg, **kw):
    for items in arg:
        yield from items


def gen_list_with_yield():
    astr = 'ABC'
    alist = [1, 2, 3]
    adict = {'name': 'tanbin', 'age': 18}
    agen = (i for i in range(4, 8))

    new_list = gen_with_yield(astr, alist, adict, agen)
    print('list from yield from: {list}'.format(list=list(new_list)))


def gen_list_with_yield_from():
    astr = 'ABC'
    alist = [1, 2, 3]
    adict = {'name': 'tanbin', 'age': 18}
    agen = (i for i in range(4, 8))

    new_list = gen_with_yield_from(astr, alist, adict, agen)
    print('list from yield from: {list}'.format(list=list(new_list)))


if __name__ == '__main__':
    gen_list_with_yield()
    gen_list_with_yield_from()
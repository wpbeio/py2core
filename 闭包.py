def counter(start_at=0):  # 相当于一个类
    count = [start_at]

    def incr():  # 类的方法
        count[0] += 1
        print(count[0])
    return incr


def main():
    count = counter(100)  # 实例化一个类，
    count()  # 调用对象的方法
    count()

    count2 = counterclass(start=1)
    count2.incr()
    count2.incr()


class counterclass(object):

    def __init__(self, start=0):
        self.start_at = start

    def incr(self):  # 类的方法
        self.start_at += 1
        print(self.start_at)


if __name__ == '__main__':
    main()

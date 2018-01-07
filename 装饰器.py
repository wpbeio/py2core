#!/usr/bin/env python


# from time import time
import time


def logged(when):
    def log(f, *args, **kargs):
        print('''called:
        function:{0}
        args:{1}
        kargs{2}
        '''.format(f, args, kargs))

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time.time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print('time delta:{0}'.format(time.time() - now))
        return wrapper
    try:
        # 按照参数返回装饰器
        return {'pre': pre_logged,
                'post': post_logged}[when]

    except KeyError as e:
        raise ValueError(e, 'must be "pre" or "post"')

# 递归算阶乘


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return(n * factorial(n - 1))


def main():
    hello("world")
    hello2('beio')


@logged('post')
def hello(name):
    time.sleep(1)
    print("hello,{0}".format(name))


@logged('pre')
def hello2(name):
    time.sleep(2)
    print("hello,{0}".format(name))


if __name__ == '__main__':
    main()

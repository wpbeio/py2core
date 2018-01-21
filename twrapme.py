#!/uer/bin/env python3
from time import time, ctime


class TimedWrapme(object):
    def __init__(self, obj):
        self.__data = obj
        # ctime 创建时间，mtime 修改的时间 atime 最后访问时间
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError("argument of 'c','m' or 'a' req 'd")
        return getattr(self, '_{0}__{1}time'.format(self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        print(ctime(self.gettimeval(t_type))) 

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __str__(self):
        self.__atime = time()
        return str(self.__data)
    #获取属性的值
    def __getattr__(self, attr):
        self.__atime = time()
        print(getattr(self.__data, attr))
def main():
    TimedWrapObj=TimedWrapme(932)
    TimedWrapObj.gettimestr('c')
    TimedWrapObj
    TimedWrapObj.gettimestr('a')
    

if __name__ == '__main__':
    main()

#！usr/bin/env python
import os
import socket
import errno
import types
import tempfile


class NetworkError(IOError):
    """网络错误"""

    def __init__(self, arg):
        super(NetworkError, self).__init__()
        self.arg = arg
    pass


class FileError(IOError):
    """文件读取错误"""

    def __init__(self, arg):
        super(FileError, self).__init__()
        self.arg = arg
    pass


def UpdArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        # 将args添加进myargs
        myargs.extend([arg for arg in args.args])
    else:
        myargs = list(args)
    if newarg:
        myargs.append(newarg)
    return tuple(myargs)


def fileArgs(file, mode, args):
    # error.EACCES 判断是否权限问题,permissienerror不可迭代
    if args.errno == errno.EACCES and 'access' in dir(os):
        perms = ''
        # r对应读成功,w对应写成功,x对应修改成功
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        # pkeys = permd.keys()
        # pkeys.sort()
        # pkeys.reverse()
        for eachPerm in 'rwx':
            # 判断是否拥有这个权限
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'
        # 如果args属于I/O错误
        if isinstance(args, IOError):
            myargs = []
            myargs.extend(arg for arg in args.args)
        else:
            myargs = list(args.args)
        myargs[1] = "'{0}'{1} (perms:'{2}')".format(mode, myargs[1], perms)

    else:
        myargs = args
    return tuple(myargs)


def myconnect(sock, host, post):
    try:
        sock.connect((host, post))
        print(host + ": ok")
    except socket.error as args:
        # print(args)
        myargs = UpdArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])
        raise NetworkError(UpdArgs(myargs, host + ':' + str(post)))


def myopen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError as args:
        raise FileError(fileArgs(file, mode, args))
    return fo


def testfile():
    # 创建缓存文件需加上模块名称
    file = tempfile.mktemp()
    f = open(file, 'w')
    f.close()
    # 八进制表示PY3使用0o开头，不适用0开头
    for eachTest in ((0, 'r'), (0o100, 'r'), (0o400, 'w'), (0o500, 'w')):
        try:
            os.chmod(file, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError as args:
            print("{2}{0}:{1}".format(args.__class__.__name__,
                                      args.arg, file + " :OpenError"))
        else:
            print(file, 'opened ok...perm ignored', eachTest)
            f.close()
    # 赋予权限,删除文件
    os.chmod(file, 0o777)
    os.unlink(file)


def testnet():
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for eachHost in ('deli', 'www.baidu.com'):
        try:
            myconnect(a, eachHost, 80)
        except NetworkError as args:
            print("{0}:{1}".format(args.__class__.__name__, args.arg))


def main():
    testfile()
    testnet()


if __name__ == '__main__':
    main()

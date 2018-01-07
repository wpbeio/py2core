#!/usr/bin/env/ python
import urllib.request

import 装饰器 as log
def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine


def firstLast(webpage):
    f = open(webpage,encoding='utf-8')
    lines = f.readlines()
    f.close()
    print(firstNonBlank(lines), end=' ')
    lines.reverse()
    print(firstNonBlank(lines), end=' ')

@log.logged('post')
def download(url='http://wwww.baidu.com', process=firstLast):
    try:
        retval = urllib.request.urlretrieve(url)[0]
    except IOError as e:
        retval = None
    if retval:
        process(retval)


def main():
    
    download()


if __name__ == '__main__':
    main()

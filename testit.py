#!/usr/bin/env python


def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)

    except Exception as e:
        result = (False, str(e))
    return result


def test():
    funcs = (int, str, float)
    vals = (123, 12.34, '1234', '12.34')
    for eachFunc in funcs:
        print('_' * 20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print('{0}(eachVal)={1}'.format(eachFunc.__name__,  retval[1]))
            else:
                print('{0}(eachVal)=FAILED:{1}'.format(
                    eachFunc.__name__,  retval[1]))


def main():
    test()


if __name__ == '__main__':
    main()

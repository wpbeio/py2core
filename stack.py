#！usr/bin/env python
stack=[]
def pushit():
    stack.append(input('输入新数据： ').strip())
def popit():
    if len(stack)==0:
        print("栈为空")
    else:
        print('移除：%s'% (stack[len(stack)-1]))
        stack.pop(len(stack)-1)

def viewstack():
    print(stack)
CMDs={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
    pr='''
p(U)sh
p(O)p
(V)iew
(Q)uit

输入选项：
    '''
    while True:
        while True:
            try:
                choice=input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choice='q'
            print('\n你输入的是：[%s]'% (choice))
            if choice not in 'uovq':
                print('输入错误')
            else:
                break
        if choice=='q':
            break
        CMDs[choice]()
if __name__ == '__main__':
    showmenu()



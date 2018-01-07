#！usr/bin/env python

while True:
    try:
        start=int(input("输入开始值:"))
    except :
        continue
    if isinstance(start,int):
        print("开始值为：",start)
        break
while True:
    try:
        end=int(input("输入结束值:"))
    except Exception as e:
        continue

    if isinstance(end,int):
        print("结束值为：",end)
        break
HasAscii=True
print('--------------------------')
if end<0 or end>255:
    HasAscii=False

print(HasAscii)



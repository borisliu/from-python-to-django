def printMax(x, y):
    '''打印两个数中的最大值。

    两个值必须是整数。'''
    # 如果可能，转换为整数
    x = int(x) 
    y = int(y)

    if x > y:
        print(x, '最大')
    else:
        print(y, '最大')

printMax(3, 5)
print(printMax.__doc__)
help(printMax)

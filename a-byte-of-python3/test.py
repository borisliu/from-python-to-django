shoplist = ['苹果', '芒果', '胡萝卜', '香蕉']
name = 'swaroop'

# 索引或下标运算 #
print('第0项是', shoplist[0])
print('第1项是', shoplist[1])
print('第2项是', shoplist[2])
print('第3项是', shoplist[3])
print('第-1项是', shoplist[-1])
print('第-2项是', shoplist[-2])
print('第0个字符是', name[0])

# 一个列表的切片 #
print('第1项到第3项是', shoplist[1:3])
print('第2项到末尾是', shoplist[2:])
print('第1到-1项是', shoplist[1:-1])
print('开头到结尾是', shoplist[:])

# 字符串的切片 #
print('第1到第3个字符是', name[1:3])
print('第2到末尾的字符是', name[2:])
print('第1到-1的字符是', name[1:-1])
print('从头到尾的字符是', name[:])
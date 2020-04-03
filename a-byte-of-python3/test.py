# 这是一个字符串对象
name = 'Swaroop' 

if name.startswith('Swa'):
    print('是的，字符串以"Swa"开始')

if 'a' in name:
    print('是的，它包含字符串"a"')

if name.find('war') != -1:
    print('是的，它包含字符串"war"')

delimiter = '_*_'
mylist = ['巴西', '俄罗斯', '印度', '中国']
print(delimiter.join(mylist))
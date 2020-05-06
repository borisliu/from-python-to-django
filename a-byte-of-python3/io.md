## 输入与输出

某些情况下，你的程序必须与用户进行交互。例如，你想获取来自用户的输入，然后给用户打印返回的结果。我们可以分别使用`input()`和`print()`函数来实现。

对于输出，我们可以使用`str`类中的方法。例如，你可以使用`rjust`方法得到一个右对齐、指定宽度的字符串。可以通过`help(str)`来查看更详细的信息。

另一个常见的输入/输出类型是处理文件。创建、读取和写入文件的能力对于很多程序来说是至关重要的，我们将在本章探索这个特性。

## 用户输入

将这个程序保存为`io_input.py`:

```python
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('输入文本：')
if (is_palindrome(something)):
    print("是的，这是回文")
else:
    print("不，这不是回文")

```

输出：

```shell
C:\> python io_input.py
输入文本： 蜜蜂
不，这不是回文
C:\> python io_input.py
输入文本： 人上人
是的，这是回文
```

**它是如何工作的：**

我们使用切片特性来反转文本。我们已经知道了如何通过`seq[a:b]`来得到位置`a`到位置`b`的[序列切片](./data_structures.md)。我们还可以提供第三个参数来决定切片的**步长**，切片默认的步长是`1`，因为这样会返回文本连续的部分。给一个负值的步长，即`-1`，会返回文本的反转。

`input()`函数将字符串作为参数，并且展示给用户。然后它会等待用户输入并按下返回键。一旦用户输入并按下了返回键，`input()`函数会将会返回用户输入的文本。

我们得到文本并反转它。如果原始文本和反转文本是相等的，那么这个文本就是一个[回文](http://en.wiktionary.org/wiki/palindrome)。

### 家庭作业

对英文来说检查一段文字是不是回文，需要忽略标点、空格和大小写。例如："Rise to vote, sir." 是一句回文，但目前版本的程序还不能认出它。你能够修改程序让它能认出这句回文吗？

如果你没有思路，请参考文末的提示。

## 文件

为了读写，你可以通过创建一个file类的对象，分别使用read、readline或 write方法来，打开和使用文件。能够读取或写入文件取决于文件打开时指定的模式。最后，当你完成对文件的操作时，你要调用close方法告诉Python，文件我们使用完了。

例子 (保存为 using_file.py):

```
poem = '''\
当工作完成时
编程是有趣的
如果想让你的工作有趣
    使用Python！
'''
 
f = open('poem.txt', 'w') # 为'写w'打开文件
f.write(poem) # 文本写入文件
f.close() # 关闭文件
 
f = open('poem.txt') # 如果不指定打开模式，默认为'读'
while True:
    line = f.readline()
    if len(line) == 0: # 0长度表示文件结尾
        break
    print(line, end='')
f.close() # 关闭文件
```

输出：

```
D:> python using_file.py
当工作完成时
编程是有趣的
如果想让你的工作有趣
    使用Python！
```

它是如何工作的：

首先，通过内置的函数open，指定文件名和我们要打开的模式，打开一个文件。模式可以是读模式('r'), 写模式('w')或追加模式('a')。我们也可以指定是否以文本格式('t') 或二进制格式('b')读,写或追加。实际上有更多可用的模式，help(open) 会给你更多的细节。默认情况下，open()认为是一个以读方式打开的文本格式的文件。

在我们的例子中，我们首先以写文本格式打开文件，使用文件对象的write方法写文件，然后,我们最后 close(关闭)文件。

接下来，为再次阅读，我们打开同一个文件。我们不需要指定一个模式,因为 '读文本文件' 是默认的模式。我们使用readline方法在一个循环中每次读文件的一行。该方法返回一个完整的行，包括换行符结束时的行。当返回一个空字符串时，这意味着我们已经到达文件的末尾，我们'打破'循环。

在默认情况下，print()函数在屏幕上自动换行打印文本。我们是通过指定end=''禁止产生新行，因为从文件读取的行在结尾已经包含一个换行符。然后，我们最终close文件。

现在，检查poem.txt的内容，确认程序确实写入和从那个文件读取。

## 拾取

Python提供了一个标准的模块称为pickle，使用它你可以在一个文件中存储**任何**的Python对象，然后把它弄回来后，这就是所谓的持续的存储对象。

例子 (保存为 pickling.py):

```
import pickle
 
# 我们将要存储对象的文件名
shoplistfile = 'shoplist.data'
# 购物清单
shoplist = ['苹果', '芒果', '胡萝卜']
 
# 定到文件
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # 把对象倒入一个文件
f.close()
 
del shoplist # 释放shoplist变量
 
# 从仓库读回
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # 从文件载入对象
print(storedlist)
```

输出：

```
D:> python pickling.py
['苹果', '芒果', '胡萝卜']
```

它是如何工作的：

要在文件中存储一个对象，我们首先必须以'w'rite写'b'inary 二进制格式的方式open打开文件，然后调用pickle模块的dump函数，这个过程叫拾取。

接下来，我们使用pickle模块的load函数取回对象，这个过程叫做拆开。

## 小结

我们已经讨论了各种类型的输入/输出，文件处理和使用pickle模块。

接下来，我们将探讨索异常的概念。


### 家庭作业提示

> 使用一个元组（从[这里](http://grammar.ccc.commnet.edu/grammar/marks/marks.htm)你可以找到所有标点符号的一个列表）来保存所有需要禁用的字符，然后使用成员资格测试来确定一个字符是否应该被移除，即 forbidden = (!, ?, ., ...)。
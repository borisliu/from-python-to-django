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

为了读写文件，你可以通过创建一个`file`类的对象，然后使用`read`、`readline`或`write`方法来打开和使用文件。对文件的读写能力取决于你打开文件时选择的模式。当你处理完文件后，你可以使用`close`方法告诉 Python 你已经使用完文件了。

例子 (保存为 io_using_file.py):

```python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件进行 'w'riting 写操作
f = open('poem.txt', 'w')
# 将文本写入到文件
f.write(poem)
# 关闭文件
f.close()

# 如果没有指定文件打开方式
# 默认使用 'r'ead 读模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零行意味着 EOF 文件结尾
    if len(line) == 0:
        break
    # `line` 中已经自带换行了
    # 因为它是从文件中读取出来的
    print(line, end='')
# 关闭文件
f.close()
```

输出：

```
C:\> python io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```

**它是如何工作的：**

通过`open`方法我们很容易就能创建一个新的文件对象。我们指定文件名和打开方式，通过内置的`open`函数打开文件，当文件不存在时则创建文件。文件有很多种打开模式，可以是：读模式（`'r'`），写模式（`'w'`）或追加模式（`'a'`）。我们也可以指定以什么方式进行读、写和追加，是文本模式（`'t'`）还是二进制模式（`'b'`）。还有很多打开模式的组合，你可以通过`help(open)`命令来查看详细的说明。默认情况下`open()`认为文件以文本模式打开进行读取操作。

在我们的例子里，第一次我们用`write`方法打开/创建了这个文件，并把字符串变量`poem`写入文件里，之后我们用`close`关闭了文件。

接下来我们再次打开同一个文件用于读取。我们不需要指定模式，因为默认的读取文件模式已经足够了。我们使用`readline`方法在一个循环中每次读取文件的一行。这个方法每次会返回包括换行符在内的一整行。当读到**空**字符时，就说明已经到了文件的结尾，我们就可以跳出（break）循环了。

最后，我们用`close`关闭了文件。

从`readline`的输出中我们可以得知：这个程序已经成功地把小诗写入了`poem.txt`文件，并可以从中读取出来，打印到屏幕上。

## 序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等。

Python提供了一个标准模块`pickle`，你可以使用该模块将**任何**简单的Python对象存储在文件中，然后可再次取回。这个过程也被称为**持久化存储对象**。

例子 (保存为`io_pickle.py`):

```python
import pickle

# 这是我们将存储对象的文件名
shoplistfile = 'shoplist.data'
# 购物的清单
shoplist = ['苹果', '芒果', '胡萝卜']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()

# 销毁 shoplist 变量
del shoplist

# 从存储中读回
f = open(shoplistfile, 'rb')
# 从文件加载对象
storedlist = pickle.load(f)
print(storedlist)
f.close()
```

输出：

```shell
C:\> python pickling.py
['苹果', '芒果', '胡萝卜']
```

**它是如何工作的：**

要将对象存储在文件中，必须先以二进制写入模式`open`文件，然后调用`pickle`模块的`dump`函数将对象保存到文件 file 中去，这个过程叫做**pickling**。

之后，我们可使用`pickle`模块的`load`函数来获取并返回这个对象。此过程称为**unpickling**。

## Unicode

到目前为止，当我们编写和使用字符串或者读取和写入文件时，我们只使用了简单的英文字符。 英语和非英语字符都可以用 Unicode 码表示（请参阅本节末尾的文章了解更多信息），默认情况下 Python 3 使用 Unicode 存储字符串变量（想想所有我们用单或双或三重引号包裹的文本）。

> 注意：如果你使用的是Python 2，并且我们希望能够读取和编写其他非英语语言，我们需要使用`unicode`类型，所有内容都以字符`u`开头，例如：`u"hello world"`。

```python
>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
```

当通过互联网发送数据时，我们需要以字节为单位发送数据，这是计算机易于理解的方式。将 Unicode 码（这是 Python 在存储字符串时使用的）转换为字节的规则称为编码。一种流行的编码方式是 UTF-8 。我们可以通过在`open`函数中使用一个简单的关键字参数来读写 UTF-8 。

```python
# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
```

**它是如何工作的：**

我们使用 `io.open` 然后在第一个 open 语句中使用 `encoding` 参数对信息进行编码，然后在解码信息时再在第二个 open 语句中使用该参数。 请注意，我们应该只在文本模式下使用 open 语句时的使用编码。

每当我们编写一个使用 Unicode 文字的程序（通过在字符串之前放置一个 `u` ）就像我们上面使用的那样，我们必须确保 Python 本身被告知我们的程序使用 UTF-8，我们必须把 `# encoding=utf-8` 注释在我们程序的顶部。

想要详细了解此主题，请阅读以下内容：

- ["The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"](http://www.joelonsoftware.com/articles/Unicode.html)
- [Python Unicode Howto](http://docs.python.org/3/howto/unicode.html)
- [Pragmatic Unicode talk by Nat Batchelder](http://nedbatchelder.com/text/unipain.html)

## 小结

我们已经讨论了各种类型的输入 / 输出操作，包括：文件处理、pickle 模块和 Unicode。

接下来，我们将探讨索异常的概念。

### 家庭作业提示

> 使用一个元组（从[这里](http://grammar.ccc.commnet.edu/grammar/marks/marks.htm)你可以找到所有标点符号的一个列表）来保存所有需要禁用的字符，然后使用成员资格测试来确定一个字符是否应该被移除，即 forbidden = (!, ?, ., ...)。
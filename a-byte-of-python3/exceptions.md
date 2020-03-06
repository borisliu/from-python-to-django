# 异常

当你的程序处于异常的状态的时候，会抛出_异常_。例如当你想要读取一个并不存在的文件的时候，或者当你要删除一个正在运行的程序的时候。这些情况通过**异常**来处理。

类似的，如果你的程序有一些无效的语句，Python也会**抛出**错误提示告诉你这里有一些**错误**。

## 错误

我们来看一下一个简单的`print`函数。如果我们把`print`写成了`Print`会怎样？注意大小写的错误。这是Python会_抛出_一个语法错误。

```python
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
```

我们注意到抛出了一个`NameError`的错误，以及这个错误发生的位置。这就是当错误发生的时候**错误处理程序**所做的事情。

## 异常

我们尝试从控制台读取用户输入的信息，然后按下`[ctrl-d]`看看会发生什么。

```python
>>> s = input('请输入 --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

Python抛出了一个名为`EOFError`的错误信息，他的是*end of file*的缩写(由`ctrl-d`触发)，这是我们的程序刚开始的时候没有预料到的。

## 异常处理

我们可以用`try..except`语句处理异常。我们将正常执行的语句放在try语句块中，然后将错误处理程序放到except语句块中。

例如 (保存为 `exceptions_handle.py`):

```python
try:
    text = input('请输入 --> ')
except EOFError:
    print('为什么你按下了EOF？')
except KeyboardInterrupt:
    print('你取消了操作')
else:
    print('你输入了 {}'.format(text))
```

输出为:

```
# 按下 ctrl + d
$ python exceptions_handle.py
请输入 --> 为什么你按下了EOF？

# Press ctrl + c
$ python exceptions_handle.py
请输入 --> ^C你取消了操作

$ python exceptions_handle.py
请输入 --> No exceptions
你输入了 No exceptions
```

**它是如何工作的：**

我们将所有的可能会抛出异常/错误的语句写在`try`块中，然后将对应的处理程序写在`except`块中。每个`except`语句可以处理一个特定的异常/错误，或者是一个异常/错误的列表（用括号表示）。如果没有指明异常/错误的名字，那么他会处理_所有的_错误/异常。

注意，每一个`try`语句至少应该有一个与之匹配的`except`语句，否则try语句就没有意义了。

如果你的程序发生了异常/错误，但是没有被处理，那么Python语言就会启动默认的异常处理程序，它会中止程序的运行，打印出错误的信息，这些内容我们已经看到了。

你也可以给你的`try..except`写上一个`else`语句块，当没有任何异常发生的时候就会执行`else`语句的内容。

在下面的例子中，我们将会学习如何获得异常对象，以便于我们能够得到关于异常的更多的信息。

## 抛出异常

你可以使用`raise`语句_抛出_一个异常，在语句中你需要提供异常/错误的名称以及抛出的异常对象。

你抛出的异常/错误必须是一个从`Exception`派生的类。

例如： (保存为`exceptions_raise.py`)：

```python
class ShortInputException(Exception):
    '''用户自定义的异常类。'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('请输入 --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
```

输出为：

```
$ python exceptions_raise.py
请输入 --> a
ShortInputException: The input was 1 long, expected at least 3

$ python exceptions_raise.py
请输入 --> abc
No exception was raised.
```

**它是如何工作的：**

在这里我们创建了我们自己的异常类。新的异常类为`ShortInputException`。他有两个字段：`length`表示输入内容的长度，`atleast`表示程序期望的最小长度。

在`except`语句中，我们制定由`as`变量保存弹出的异常/错误的对象。这很类似函数参数在函数调用中的作用。在这个特殊的`except`语句中，我们使用异常对象的`length`和`atleast`字段构造了一个异常提示信息，让用户了解为什么会抛出这个异常。

## Try ... Finally

设想一下你的程序需要读取一个文件，你怎样保证无论是否有异常抛出，文件对象都被正确的关闭呢？我们可以使用`finally`语句块做到这一点。

例如：（保存为`exceptions_finally.py`）

```python
import sys
import time

f = None
try:
    f = open("poem.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
```

输出为：

```
$ python exceptions_finally.py
Programming is fun
Press ctrl+c now
^C!! You cancelled the reading from the file.
(Cleaning up: Closed the file)
```

**它是如何工作的：**

我们读取文件的内容，只是每读一行就让系统休息2秒，我们使用`time.sleep`函数让程序运行慢一点（正常情况下Python程序运行的飞快）。当程序还在运行的时候，按下`ctrl + c`键中止程序的运行。

我们注意到当程序退出的时候抛出了`KeyboardInterrupt`异常。然而，在程序退出之前，执行了finally语句块，并且文件对象被正确的关闭了。

注意，我们在`print`函数后面调用`sys.stdout.flush()`函数，这样可以及时输出结果。

## with语句

在`try`语句块中获取资源，然后再`finally`语句块中释放资源是一个非常常用的程序段，我们可以使用`with`简化一下程序的书写。

例如：（保存为`exceptions_using_with.py`）

```python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
```

**它是如何工作的：**

这段程序的输出应该和之前的例子是一模一样的。唯一的区别在与我们在`with`语句中使用`open`函数打开文件，这样的话系统会自动关闭这个文件。

实际的处理过程是这样的，`with`语句会获取`open`函数返回的对象，我们假定这个对象名称是"thefile"。

它_总是会_在进入`with`语句块之前调用`thefile.__enter__`函数，并且_总是会_在语句块的最后调用`thefile.__exit__`函数。

这样的话我们之前在`finally`语句块中写的程序就会自动的在`__exit__`方法中被执行，这种方式可以防止我们频繁使用`try..finally`语句。

关于这个主题更多的讨论已经超出了本书的范畴，请参考[PEP 343](http://www.python.org/dev/peps/pep-0343/)。

## 总结

本章我们讨论了`try..except`和`try..finally`语句，我们还自己定义了一个我们自己的异常类型，并且在程序中将其抛出。

下一步，我们将会浏览一下Python标准库。

--------------------------------------------------

### 继续阅读[标准库](stdlib.md)
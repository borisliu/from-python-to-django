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

You can _raise_ exceptions using the `raise` statement by providing the name of the error/exception and the exception object that is to be _thrown_.

The error or exception that you can raise should be a class which directly or indirectly must be a derived class of the `Exception` class.

Example (save as `exceptions_raise.py`):


Output:


**How It Works**

Here, we are creating our own exception type. This new exception type is called `ShortInputException`. It has two fields - `length` which is the length of the given input, and `atleast` which is the minimum length that the program was expecting.

In the `except` clause, we mention the class of error which will be stored `as` the variable name to hold the corresponding error/exception object. This is analogous to parameters and arguments in a function call. Within this particular `except` clause, we use the `length` and `atleast` fields of the exception object to print an appropriate message to the user.

## Try ... Finally {#try-finally}

Suppose you are reading a file in your program. How do you ensure that the file object is closed properly whether or not an exception was raised? This can be done using the `finally` block.

Save this program as `exceptions_finally.py`:


Output:


**How It Works**

We do the usual file-reading stuff, but we have arbitrarily introduced sleeping for 2 seconds after printing each line using the `time.sleep` function so that the program runs slowly (Python is very fast by nature). When the program is still running, press `ctrl + c` to interrupt/cancel the program.

Observe that the `KeyboardInterrupt` exception is thrown and the program quits. However, before the program exits, the finally clause is executed and the file object is always closed.

Note that we use `sys.stdout.flush()` after `print` so that it prints to the screen immediately.

## The with statement {#with}

Acquiring a resource in the `try` block and subsequently releasing the resource in the `finally` block is a common pattern. Hence, there is also a `with` statement that enables this to be done in a clean manner:

Save as `exceptions_using_with.py`:


**How It Works**

The output should be same as the previous example. The difference here is that we are using the `open` function with the `with` statement - we leave the closing of the file to be done automatically by `with open`.

What happens behind the scenes is that there is a protocol used by the `with` statement. It fetches the object returned by the `open` statement, let's call it "thefile" in this case.

It _always_ calls the `thefile.__enter__` function before starting the block of code under it and _always_ calls `thefile.__exit__` after finishing the block of code.

So the code that we would have written in a `finally` block should be taken care of automatically by the `__exit__` method. This is what helps us to avoid having to use explicit `try..finally` statements repeatedly.

More discussion on this topic is beyond scope of this book, so please refer [PEP 343](http://www.python.org/dev/peps/pep-0343/) for a comprehensive explanation.

## Summary

We have discussed the usage of the `try..except` and `try..finally` statements. We have seen how to create our own exception types and how to raise exceptions as well.

Next, we will explore the Python Standard Library.

--------------------------------------------------

### 继续阅读[标准库](stdlib.md)
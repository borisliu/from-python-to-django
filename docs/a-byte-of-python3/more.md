# 更多

迄今为止我们已经学习了Python中的大多数常用知识。本章中我们会接触到更多的知识，使得我们更全面的掌握Python。

## 传递元组

你是否希望过从函数返回两个不同的值？做到这点使用元组即可。

```python
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
```

注意，我们使用`a, b = <some expression>`这个表达式把元组的两个字段分别赋给两个变量。

这也意味着在Python中最快速的交换两个变量的值得方法是：

```python
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

## 特殊方法

有一些诸如__intit__和__del__的方法在类中拥有特殊的含义。

特殊方法用于模拟某些内建类型的行为。例如，你希望为你的类使用`x[key]`索引操作(就像在列表和元组中那样)，那么你仅仅需要实现`__getitem__`方法就可以了。顺便提一句，Python正是这样实现`list`类的！

一些有用的特殊方法列在下表中。如果你想了解所有的特殊方法，详见[帮助文档](http://docs.python.org/3/reference/datamodel.html#special-method-names).

- `__init__(self, ...)`
    - 在对象第一次被创建后，返回之前调用。

- `__del__(self)`
    - 在对象被销毁前调用（我们无法预期这个函数什么时候被调用，因此尽量避免使用它）。

- `__str__(self)`
    - 在使用`print`函数或`str()`时调用。

- `__lt__(self, other)`
    - 在使用_小于_运算符时(<)调用。类似的其它运算符也存在对象的特殊方法(+, >等)。

- `__getitem__(self, key)`
    - 当使用`x[key]`索引操作时调用。

- `__len__(self)`
    - 当使用内建`len()`函数时调用，一般用于序列的对象。

## 单语句块

我们已经看到每个语句块都根据它的缩进级别将彼此区分开。不过有一个例外，如果某语句块只包含单条语句，你可以把它放到同一行，例如条件语句或循环语句。下面的例子清楚的说明了这点：

```python
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

注意上面的单条语句被放置到同一行而没有作为单独的块。虽然你利用这点可以让程序变的_更短_，但我强烈建议你避免使用这个快捷方式(除了错误检测)，主要原因是使用适当的缩进可以更方便的添加额外的语句。

## Lambda表达式

`lambda`语句用于在运行时创建新的函数对象。通常情况下`lambda`语句带有一个参数，后面跟着一个简单的表达式作为函数体，把参数代入函数得到的返回值就是新的函数的返回值。

例如 (保存为`more_lambda.py`):

```python
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
```

输出:

```
$ python more_lambda.py
[{'y': 1, 'x': 4}, {'y': 3, 'x': 2}]
```

**它是如何工作的：**

注意，`list`对象的`sort`函数有一个名为`key`的参数决定了这个列表是怎样被排序的（通常情况下为升序或者降序）。在我们的例子中，我们想要有一个自己的排序规则，我们需要写一个比较函数，而不是使用`def`定义一个只在这里使用一次的函数，因此我们使用lambda表达式创建一个新的函数。

## 列表解析

列表解析用于从一个现有的列表派生出一个新的列表。 假设你有一个数字列表，你想让其中所有大于2的元素乘以2并组成一个新的列表。类似问题正是使用列表解析的理想场合。

例子 (保存为`more_list_comprehension.py`):

```python
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)
```

输出:

```
$ python more_list_comprehension.py
[6, 8]
```

**它是如何工作的：**

当某些条件满足时(`if i > 2`)我们执行某些操作(`2 * i`)，由此产生一个新列表。注意原始列表并不会被改变。

使用列表解析的好处在于，当我们使用循环遍历元素并将其存储到新列表时可以减少样板代码量。

## 函数接收元组和列表

这里有一种特殊的方法可以将函数的形参当做元组或字典，那就是分别使用`*`和`**`前缀。
当需要在函数内得到可变数量的实参时这个方法很有用。

```python
>>> def powersum(power, *args):
...     '''Return the sum of each argument raised to the specified power.'''
...     total = 0
...     for i in args:
...         total += pow(i, power)
...     return total
...
>>> powersum(2, 3, 4)
25
>>> powersum(2, 10)
100
```

因为`args`变量带有`*`前缀，因此所有额外的实参都会被当做一个元组存入`args`中并传给函数。
如果把这里的`*`换成`**`，则所有额外的形参都会被当做一个字典的键/值对。

## assert语句

`assert`用于断言一个表达式为真。例如，你需要确保正在使用的列表至少有一个元素，否则引发一个错误，这种情况很适合使用`assert`语句。
当assert语句断言失败，则引发一个`AssertError`。

```python
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

`assert`应当慎重使用。多数时候用于捕获异常，处理问题或是向用户显示错误后随即终止程序。

## 装饰器(decorator)

Decorators are a shortcut to applying wrapper functions. This is helpful to "wrap" functionality with the same code over and over again. For example, I created a `retry` decorator for myself that I can just apply to any function and if any exception is thrown during a run, it is retried again, till a maximum of 5 times and with a delay between each retry. This is especially useful for situations where you are trying to make a network call to a remote computer:

```python
from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")


def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapped_f


counter = 0


@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    # This will throw an exception in the first call
    # And will work fine in the second call (i.e. a retry)
    if counter < 2:
        raise ValueError(arg)


if __name__ == '__main__':
    save_to_database("Some bad value")
```

输出:

```
$ python more_decorator.py
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.
ERROR:retry:Attempt 1/5 failed : (('Some bad value',), {})
Traceback (most recent call last):
  File "more_decorator.py", line 14, in wrapped_f
    return f(*args, **kwargs)
  File "more_decorator.py", line 39, in save_to_database
    raise ValueError(arg)
ValueError: Some bad value
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.
```

**它是如何工作的：**

See:

- http://www.ibm.com/developerworks/linux/library/l-cpdecor.html
- http://toumorokoshi.github.io/dry-principles-through-python-decorators.html

## Differences between Python 2 and Python 3 {#two-vs-three}

See:

- ["Six" library](http://pythonhosted.org/six/)
- [Porting to Python 3 Redux by Armin](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
- [Python 3 experience by PyDanny](http://pydanny.com/experiences-with-django-python3.html)
- [Official Django Guide to Porting to Python 3](https://docs.djangoproject.com/en/dev/topics/python3/)
- [Discussion on What are the advantages to python 3.x?](http://www.reddit.com/r/Python/comments/22ovb3/what_are_the_advantages_to_python_3x/)

## Summary

We have covered some more features of Python in this chapter and yet we haven't covered all the features of Python. However, at this stage, we have covered most of what you are ever going to use in practice. This is sufficient for you to get started with whatever programs you are going to create.

Next, we will discuss how to explore Python further.

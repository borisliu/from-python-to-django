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

## Lambda Forms

A `lambda` statement is used to create new function objects. Essentially, the `lambda` takes a parameter followed by a single expression only which becomes the body of the function and the value of this expression is returned by the new function.

Example (save as `more_lambda.py`):

<pre><code class="lang-python">{% include "./programs/more_lambda.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/more_lambda.txt" %}</code></pre>

**How It Works**

Notice that the `sort` method of a `list` can take a `key` parameter which determines how the list is sorted (usually we know only about ascending or descending order). In our case, we want to do a custom sort, and for that we need to write a function but instead of writing a separate `def` block for a function that will get used in only this one place, we use a lambda expression to create a new function.

## List Comprehension

List comprehensions are used to derive a new list from an existing list. Suppose you have a list of numbers and you want to get a corresponding list with all the numbers multiplied by 2 only when the number itself is greater than 2. List comprehensions are ideal for such situations.

Example (save as `more_list_comprehension.py`):

<pre><code class="lang-python">{% include "./programs/more_list_comprehension.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/more_list_comprehension.txt" %}</code></pre>

**How It Works**

Here, we derive a new list by specifying the manipulation to be done (`2*i`) when some condition is satisfied (`if i > 2`). Note that the original list remains unmodified.

The advantage of using list comprehensions is that it reduces the amount of boilerplate code required when we use loops to process each element of a list and store it in a new list.

## Receiving Tuples and Dictionaries in Functions

There is a special way of receiving parameters to a function as a tuple or a dictionary using the `*` or `**` prefix respectively. This is useful when taking variable number of arguments in the function.

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

Because we have a `*` prefix on the `args` variable, all extra arguments passed to the function are stored in `args` as a tuple.  If a `**` prefix had been used instead, the extra parameters would be considered to be key/value pairs of a dictionary.

## The assert statement {#assert}

The `assert` statement is used to assert that something is true. For example, if you are very sure that you will have at least one element in a list you are using and want to check this, and raise an error if it is not true, then `assert` statement is ideal in this situation. When the assert statement fails, an `AssertionError` is raised.

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

The `assert` statement should be used judiciously. Most of the time, it is better to catch exceptions, either handle the problem or display an error message to the user and then quit.

## Decorators {#decorator}

Decorators are a shortcut to applying wrapper functions. This is helpful to "wrap" functionality with the same code over and over again. For example, I created a `retry` decorator for myself that I can just apply to any function and if any exception is thrown during a run, it is retried again, till a maximum of 5 times and with a delay between each retry. This is especially useful for situations where you are trying to make a network call to a remote computer:


Output:


**How It Works**

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

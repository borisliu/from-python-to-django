# 模块

您已经看到如何通过定义函数在程序中重用代码。如果你想在其它程序中重用一组函数，怎么办？你可能已经猜到了，答案就是模块。

编写模块有各种各样的方法，但是最简单的方法是创建一个以`.py`为扩展名，包含函数和变量的文件。

编写模块的另一种方式就像是编写Python解释器一样，可以使用[C 编程语言](http://docs.python.org/3/extending/index.html)编写模块。当它们被编译后，当使用标准的Python解释器时，你可以在Python代码中使用这些模块。

一个模块可以通过**imported(导入)**另一个程序而使用其功能。我们可以通过同样的方法使用Python标准库。首先 ,我们看一下如何使用标准库模块。

例子 (保存为module_using_sys.py):

```python
import sys

print('命令行参数是：')
for i in sys.argv:
    print(i)

print('\n\nPYTHONPATH是', sys.path, '\n')
```

输出:

```
$ python module_using_sys.py we are arguments
命令行参数是：
module_using_sys.py
we
are
arguments


PYTHONPATH是 ['d:\\KanCloud\\from-python-to-django\\a-byte-of-python3', 'C:\\Users\\boris\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 
# 还有很多，这里不一一列出
'C:\\Users\\boris\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']


```

**它是如何工作的:**

首先，我们使用`import`语句**import(导入)**`sys`（系统）模块。通常情况下，这意味着我们告诉Python，我们想使用这个模块。`sys`模块包含了与Python解释器和其运行环境（如操作系统）有关的函数。

当Python执行`import sys`语句时，它会查找`sys`模块。在这里，它是一个内建模块，因此，Python知道到去哪里找到它。

如果它还没有被编译，也就是Python的源代码，那么，Python解释器将在`sys.path`目录列表中搜索。如果找到了这个模块，那么就执行模块中的代码，对你的程序来说，这个模块就变成**有效**的。注意，初始化只有在我们**第一次**导入一个模块时完成。

我们通过点符号访问`sys`模块中的`argv`变量，就像这样`sys.argv`。它表明，`argv`这个名字是`sys`模块的一部分。这种方法的另一个优点是，如果你的程序中使用了名为`argv`的变量，那么他们不会冲突。

`sys.argv`变量一个字符串**list(列表)**（我们会在[后面的章节](./data_structures.md)详细介绍）。具体来说，`sys.argv`包含**命令行参数**的列表，也就是使用命令行向你的程序传递的参数清单。

如果您正在使用IDE编写并运行这些程序，在菜单中寻找一种方法来指定命令行参数传递给你的程序。

这里，当我们执行`python module_using_sys.py we are arguments`时，我们使用 `python`命令和后面的参数运行`module_using_sys.py`模块。Python把命令行参数存储在`sys.argv`变量中供我们使用。

记住，运行脚本的名字通常是`sys.argv`列表中的第一个参数。因此，这里的`sys.argv[0]`是`'module_using_sys.py'`，`sys.argv[1]`是`'we'`，`sys.argv[2]`是`'are'`和`sys.argv[3]`是`'arguments'`。注意，Python从0而不是1开始计数。

`sys.path`包含可以被导入的模块所在的目录名列表。我们注意到`sys.path`的第一个字符串就是程序的当前路径。这意味着你可以直接导入位于当前目录中的模块。否则，你必须把你的模块放在`sys.path`列表中的一个目录中。

请注意，当前目录是程序启动的目录。运行`import os; print(os.getcwd())`找到你的程序的当前目录。

## 字节编译的.pyc文件

导入整个模块是一个代价相对较高的事情，所以Python提供了一些技巧使它可以效率更高。一种方法是创建扩展名为`.pyc`的**字节编译**文件，这是Python将程序转换成的一种中间形式(我们在[简介](introduction.md)中介绍过Python是如何工作的。当你下次从一个不同程序导入模块时，这种`.pyc`文件是有很用的--它将快得多，因为导入模块一部分需要处理的工作已经完成了。同时，这些字节编译的文件是与操作系统平台无关的。

注意：这些`.pyc`文件通常在与之相应的`.py`文件的同一个目录中创建。如果Python在那个目录中没有写入权限，那么就**无法**创建`.pyc`文件。

## from ... import语句

如果你想直接导入`argv`变量到程序中(为了避免每次为它键入`sys.`)，可以使用`from sys import argv`语句。

> 一般来说，应该**避免**使用这个语句，尽量使用`import`语句，这样可以在程序中避免名称冲突，使你的程序更具有可读性。

例如：

```python
from math import sqrt
print("16的平方根是", sqrt(16))
```

## 模块的`__name__`

每个模块都有一个名字，在模块内部的语句可以获得它所在的模块的名字。当我们想搞清楚模块是直接运行还是被导入的时候，这种设计很方便。前面提到过，当一个模块被第一次导入时，其所包含的代码被执行。我们可以通过使用这个特性，根据模块是直接运行还是从另一个模块被导入，执行不同的操作。我们可以通过使用模块的`__name__`属性来实现上述功能。

例子 (保存为 module_using_name.py):

```python
if __name__ == '__main__':
    print('这个程序正在被自己运行')
else:
    print('我从别的模块被导入')
```

输出：

```shell
C:\> python module_using_name.py
这个程序是直接运行的
C:\> python3
>>> import using_name
我从被别的模块导入
>>>
```

**它是如何工作的：**

每个Python模块都会定义自己的`__name__`，如果是`'__main__'`，这意味着模块在被用户直接运行，我们可以执行相应的操作。

## 制作属于你自己的模块

创建自己的模块是很容易的，就像你一直在这样的那样。因为每个Python程序就是一个模块。你只需要确保它有一个`.py`扩展名。下面的例子会让你明白这一点。

例子 (保存为mymodule.py):

```python
def say_hi():
    print('嗨，这就是我的模块。')

__version__ = '0.1'
```

上面的是**模块**的一个例子。正如您看到的，和我们通常的Python程序相比，没有什么特别的。接下来我们看一下如何在我们其它的程序中使用这个模块。

记住，该模块要么放置在我们导入它的程序同一个目录中，要么放置在`sys.path`目录列表中的一个目录中。

另一个模块(保存为mymodule_demo.py):

```python
import mymodule

mymodule.say_hi()
print('版本', mymodule.__version__)
```

输出：

```shell
C:\> python mymodule_demo.py
嗨，这就是我的模块。
版本 0.1

```

**它是如何工作的：**

注意，我们使用相同的点符号来访问模块的成员。Python充分重用相同的符号产生了独特的'Pythonic'的感觉，这样我们不需要总是学习新的方法来做事情。

这是使用`from..import`语法的一个版本(保存为mymodule_demo2.py):

```python
from mymodule import say_hi, __version__

say_hi()
print('版本', __version__)
```

`mymodule_demo2.py`和`mymodule_demo.py`的输出相同。

注意，如果在导入模块中已经有一个`__version__`名字的声明，这里会有一个冲突。这也可能是因为它是常见的做法--对于每个模块使用这个名字声明它的版本号。因此，我们推荐使用`import`语句，虽然它可能让你的程序有点长。

你还可以使用：

```python
from mymodule import *
```

这将导入所有的公共名称如 say_hi，但不会导入__version__，因为它始于双下划线。

> 注意：尽量不要使用`import *`这种方式，诸如`from mymodule import *`等

<!-- -->

> **Python之禅**
> 
> Python的一个指导原则是"显式优于隐式"。运行`import this`去学习更多相关的信息。

## `dir`函数

您可以使用内置的`dir()`函数列出一个对象定义的标识符。例如，对于一个模块，包括在模块中已经定义的函数、类和变量。

`dir()`函数有参数。当你给`dir()`提供一个模块名字时，它返回在那个模块中定义的名字的列表。当没有为其提供参数时, 它返回当前模块中定义的名字的列表。

例如：

```shell
C:\>python

>>> import sys 

# 获得属性列表，在这里是sys模块的属性列表
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']

# 获得当前模块的属性列表
>>> dir() 
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']

# 创建了一个新变量 'a'
>>> a = 5 

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'sys']

# 删除/移除一个名字
>>> del a 

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']

>>>
```

**它是如何工作的：**

首先，我们在导入的`sys`模块上使用`dir`。我们能看到模块包含的巨大的属性列表。

然后，我们使用没有传递参数的`dir`函数。默认情况下，它返回当前模块的属性列表。注意，导入的模块仍然是这个列表的一部分。

为了看到`dir`在起作用，我们定义了一个新的变量`a`，并为其赋值，然后检查`dir`，我们发现列表中添加了一个同名变量。我们使用`del`语句移除当前模块的变量或属性，在`dir`函数的输出中变化再次得到体现。

关于`del`的一点注意事项--这个语句用于**删除**一个变量/属性，语句运行后（这里是`del a`），你不能再访问变量`a`--就像它从来根本没有存在过。

注意，`dir()`函数对**任何**对象都起作用。例如，运行`dir('str')`来学习`str`(string)类型的更多知识。

还有一个[`vars()`](http://docs.python.org/3/library/functions.html#vars)函数可以列出所有的属性及其值，但并不是在所有情况下都起作用。

## 包（Packages）

现在，你必须开始观察组织你的程序的层次结构。变量通常在函数内部。函数和全局变量通常在模块内部。如果你想组织模块？这就涉及到打包了。

包只是模块的文件夹，使用一个特殊的`__init__.py`文件，告诉Python这个文件夹是特殊的，因为它包含Python模块。

假设你想创建一个叫做'世界'的程序包，分装'亚洲'、'非洲'等等，分包按序包含'印度'、'马达加斯加'等等。

这是你的文件结构：

```
- <在sys.path中现有的一些文件夹>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

包只是为了方便按照层次组织模块。在[Python标准库](./stdlib.md)中，你会看到包的许多实例。

## 小结

就像函数是可重用的一部分程序一样，模块也是可重用的程序。包是组织模块的更高一级的层次结构。Python自带的标准库是一系列包和模块的例子。

我们已经看到了如何使用这些模块和创建我们自己的模块。

接下来，我们将学习一些有趣的称为数据结构的概念。 

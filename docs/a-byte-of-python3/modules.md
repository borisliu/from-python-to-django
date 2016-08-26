# 模块

您已经看到如何通过一次定义函数在程序中重用代码。如果你想在其它程序中重用一定数量的函数，你将写什么？正如你可能已经猜到了，答案是模块。

编写模块有各种各样的方法，但是最简单的方法是创建一个以.py 为扩展名、包含函数和变量的文件。

编写模块的另一种方式是使用编写Python解释器本身的本机语言，例如，你可以使用[C 编程语言](http://docs.python.org/3/extending/index.html)编写模块，当它们被编译后，当使用标准的Python解释器时，在你Python代码中可以使用这些模块。

一个模块可以因另一个程序使用其功能而被*imported(导入)*。同样，我们可以使用Python标准库。首先 ,我们将看到如何使用标准库模块。

例子 (保存为 using_sys.py):

```
import sys

print('命令行参数是：')
for i in sys.argv:
    print(i)

print('\n\nPYTHONPATH在', sys.path, '\n')
```

输出:

```
D:> python using_sys.py we are arguments
命令行参数是
using_sys.py
we
are
arguments

PYTHONPATH在[<nowiki>''</nowiki>, 'C:\\Windows\\system32\\python30.zip',
'C:\\Python30\\DLLs', 'C:\\Python30\\lib',
'C:\\Python30\\lib\\plat-win', 'C:\\Python30', 
'C:\\Python30\\lib\\site-packages']
```

它是如何工作的:

首先,我们使用import语句import导入sys（系统）模块。基本上，这意味着我们我们想告诉Python，我们想使用这个模块。sys模块包含了与Python解释器和其环境即system系统有关的函数。

当Python执行import sys 语句时，它查找sys模块。在这里，它是一个内建模块，因此，Python知道到去哪里找到它。

如果它不是一个编译的，也就是用Python写的模块，那么，Python解释器将在sys.path变量列表中的目录中搜索。如果模块被发现，那么，模块中的代码将运行，对你来说，使用模块变为有效。注意，初始化只有在我们第一次导入一个模块时完成。

在sys模块中的argv变量是通过点符号访问的，例如，例如，sys.argv。它清楚地表明，这个名字是sys模块的一部分。这种方法的另一个优点是，这个名字与你的程序中使用的任何argv变量都不冲突。

sys.argv变量一个字符串list(列表)。具体来说，sys.argv包含命令行参数，也就是使用命令行向你的程序传递参数，的列表。

如果您正在使用IDE编写并运行这些程序，在菜单中寻找一种方法来指定命令行参数传递给你的程序。

这里，当我们执行python using_sys.py we are arguments时，我们使用 python命令和其后的传递给程序的参数运行using_sys.py模块。Python把命令行参数存储在 sys.argv变量中供我们使用。

记住，运行脚本的名字通常是sys.argv列表中的第一个参数。因此，在这里将有'using_sys.py'作为sys.argv[0]，'we'作为sys.argv[1]，'are'作为sys.argv[2]和'arguments'作为sys.argv[3]。注意，Python从0而不是1开始数数。

sys.path包含被导入的模块所在的目录名列表。观察到sys.path就是的第一个字符串是空的——这个空字符串表示当前目录是和PYTHONPATH环境变量相同的、sys.path变量的一部分。这意味着你可以直接导入位于当前目录中的模块。否则，你将不得不把你的模块存放在sys.path列表中的一个目录中。

请注意，,当前目录是程序启动的目录。运行import os; print(os.getcwd())找到你的程序的当前目录。

## 字节编译的.pyc文件

导入一个模块是一个相对昂贵的事情，所以Python做 了一些技巧使它更快。一种方法是创建扩展名为.pyc的字节编译文件，是Python将程序转换成的一种中间形式。(记得在Python如何工作的[简介部分)(#介绍))。当你下次从一个不同程序导入模块时，这种.pyc文件是有很用的--它将快得多，因为导入模块一部分需要的处理已经完成。同时，这些字节编译的文件是独立于平台的。

注意
> 这些.pyc文件通常在与之相应的.py文件的同一个目录中创建。如果Python在那个目录中没有写入权限，那么.pyc文件将不会创建。

## from ... import语句

如果你想直接导入argv变量到程序中(为了避免每次为它键入sys.)，那么您可以使用from sys import argv语句。

一般来说，你应该避免使用这个语句，而应该使用import语句，因为你的程序将避免名称冲突，将更具可读性。

例如：

```
from math import sqrt
print("16的平方根是", sqrt(16))
```

## 模块的name

每个模块都有一个名字，在模块中的语句能够找出它所在的模块的名字。这对于搞清楚模块是否正在运行或被导入这样的特殊用途是很方便的。正如前面提到的，当一个模块被第一次导入时，其所包含的代码被执行。我们可以通过使用这个，根据模块是否被自己使用或从另一个 模块被导入，使模块以不同的方式起作用，这些可以通过使用模块的 __name__属性来实现。

例子 (保存为 using_name.py):

```
if __name__ == '__main__':
    print('这个程序正在被自己运行')
else:
    print('我从别的模块被导入')
```

输出：

```
D:> python using_name.py
这个程序正在被自己运行
D:> python3
>>> import using_name
我从别的模块被导入
>>>
```

它是如何工作的：

每个Python模块有其__name__ 定义，如果是__name__ ，这意味着模块在被用户独立的运行，我们可以采取适当的行动。 ## 制作属于你自己的模块

创建自己的模块是很容易的，你一直在这样做，始终都是！这是因为每个Python程序也是一个模块。 你只需要确保它有一个.py扩展名。下面的例子会让你明白。

例子 (保存为mymodule.py):

```
def sayhi():
    print('嗨，这是我的模块在讲话。')

__version__ = '0.1'
```

上面的是模块的一个示例。正如您可以看到的，和我们通过的Python程序相比，没有什么特别的。接下来我们要看如何在我们的其它程序中使用这个模块。

记住,该模块要么放置在我们导入它的程序相同的目录中，要么放置在sys.path目录列表中的一个目录中。

另一个模块(保存为mymodule_demo.py):

```
import mymodule

mymodule.sayhi()
print ('版本', mymodule.__version__)
```

输出：

```
D:> python mymodule_demo.py
嗨，这是我的模块在讲话。
版本 0.1
```

它是如何工作的：

注意，我们使用相同的点符号来访问模块的成员。Python充分重用相同的符号产生了独特的'神谕的'的感觉，这样我们不需要不断学习新的方法来做事情。

这是使用from..import语法的一个版本(保存为mymodule_demo2.py):

```
from mymodule import sayhi, __version__

sayhi()
print('版本', __version__)
```

mymodule_demo2.py和mymodule_demo.py的输出相同。

注意，如果在导入模块中已经有一个__version__名字的声明，这里会有一个冲突。这也可能是因为它是常见的做法--对于每个模块使用这个名字声明它的版本号。因此，总是推荐选择import语句，虽然它可能让你的程序有点长。

你还可以使用：

```
from mymodule import *
```

这将导入所有的公共名称如 sayhi，但不会导入__version__，因为它始于双下划线。

Python的禅
> Python的一个指导原则是"显式优于隐式"。运行import this去学习更多，看[关于Python之禅的讨论](http://stackoverflow.com/questions/228181/zen-of-python)，那里列出了每个原则的例子。

## dir函数

您可以使用内置的dir函数列出一个定义对象的标识符。例如,对于一个模块，包括在模块中定义的函数，类和变量。

当你给dir()提供一个模块名字时，它返回在那个模块中定义的名字的列表。当没有为其提供参数时, 它返回当前模块中定义的名字的列表。

例如：

```
D:> python

>>> import sys # 获得属性列表，在这里是sys模块的属性列表

>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__s
tderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_compact_freelists',
'_current_frames', '_getframe', 'api_version', 'argv', 'builtin_module_names', '
byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle'
, 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable',
'exit', 'flags', 'float_info', 'getcheckinterval', 'getdefaultencoding', 'getfil
esystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
'gettrace', 'getwindowsversion', 'hexversion', 'intern', 'maxsize', 'maxunicode
', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platfor
m', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setprofile', 'setrecursionlimit
', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_in
fo', 'warnoptions', 'winver']

>>> dir() # 获得当前模块的属性列表
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

>>> a = 5 # 创建了一个新变量 'a'

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a', 'sys']

>>> del a # 删除/移除一个名字

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

>>>
```

它是如何工作的：

首先，我们看到在导入sys模块上使用使用dir。我们能看到模块包含的巨大的属性列表。

然后，我们使用没有传递参数的dir函数。默认情况下，它返回模块的属性的列表。注意，导入模块的列表仍然是这个列表的一部分。

为了看到 dir在起作用，我们定义了一个新的变量，并为其赋值，然后检查dir，我们发现列表中添加了一个同名变量。我们使用del语句移除当前模块的变量或属性，在 del函数的输出中变化再次得到体现。

关于del的一点注意事项--这个语句用于删除一个变量/属性，语句运行后，这里是del a，你不能再访问变量a--就像它从来根本没有存在过。

注意，dir()函数对任何对象都起作用。例如，运行dir('print')来学习print函数的属性的更多知识，或运行dir(str)学习str类的属性的更多知识。

## 打包（封装）

现在，你必须开始观察组织你的程序的层次结构。变量通常在函数内部。函数和全局变量通常在模块内部。如果你想组织模块？这就到了牵涉到打包的地方了。

包只是模块的文件夹，使用一个特殊的__init__.py 文件，指示Python，这个文件夹是特殊的，因为它包含Python模块。

假设你想创建一个叫做'世界'的程序包，分装'亚洲'、'非洲'等等，分包按序包含'印度'、'马达加斯加'等等。

这是你将组织的文件夹： ~ - <在sys.path中现有的一些文件夹>/ - world/ - init.py - asia/ - init.py - india/ - init.py - foo.py - africa/ - init.py - madagascar/ - init.py - bar.py ~

包只是为了分层次组织模块的方便。在标准库中，你会看到包的许多实例。

## 小结

就像函数是可重用的部分的程序一样，模块也是可重用的程序。包是组织模块的另一个层次结构。来自Python的标准库，是包和模块的集合中的一个例子。

我们已经看到了如何使用这些模块和创建我们自己的模块。

接下来，我们将学习一些有趣的称为数据结构的概念。 


--------------------------------------------------

### 继续阅读[数据结构](data_structures.md)
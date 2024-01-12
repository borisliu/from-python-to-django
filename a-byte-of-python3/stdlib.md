# 标准库

Python标准库包括大量实用的模块，是每个 Python 标准安装的一部分。熟悉 Python 标准库是非常重要的，因为如果你了解这些库可以完成事情的范围，很多问题可以快速解决。

我们会快速浏览一下最常用的标准库模块，如果你想查看 Python 标准库的完整文档，请访问[标准库参考](http://docs.python.org/3/library/)，这份文档随着 Python 安装包也安装在你的电脑上。

接下来让我们一起探索一些有用的模块。

> 注意：如果你发现本章讨论的问题太过深奥，你可以略过本章。然而，我强烈建议你在熟练掌握 Python 编程技能之后再返回头过来看看本章的内容。

## `sys`模块

`sys` 模块包括一些与操作系统相关的功能。我们已经知道了 `sys.argv` 可以列出命令行的参数列表。

假定我们想要检查我们使用的 Python 版本，我们可以使用 `sys` 模块完成这个工作。

```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

**它是如何工作的**

`sys` 模块包含了一个名为 `version_info` 的元组，保存着 Python 软件的版本信息，其中第一项为主版本号， 我们可以通过读取这些内容来使用它。

## 日志模块

如果你想要输出调试信息，或者保存其他一些重要信息，以便于你可以随时调取，用来检查你的程序是否按照预期在运行。该怎么办？可以使用 `logging` 模块。

保存为 `stdlib_logging.py`：

```python
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

```

输出为：

```
$ python stdlib_logging.py
Logging to /Users/swa/test.log

$ cat /Users/swa/test.log
2014-03-29 09:27:36,660 : DEBUG : Start of the program
2014-03-29 09:27:36,660 : INFO : Doing something
2014-03-29 09:27:36,660 : WARNING : Dying now
```

在命令行中使用 `cat` 命令读取 'test.log' 文件的输出。如果 `cat` 命令不可用，你可以使用一个Visual Studio Code打开 `test.log` 。

**它是如何工作的**

我们使用了 Python 标准库的三个模块： `os` 模块用于和操作系统进行交互， `platform` 模块用于获取运行平台（如操作系统）的信息， `logging` 模块用于记录日志。

首先，我们调用 `platform.platform()` 来检查程序运行的操作系统（更详细的信息请参考 `import platform; help(platform)` ）。如果是 Windows 操作系统，我们找到要主驱动器、用户根文件夹和文件名。我们把这三个信息拼接起来，就得到了日志文件的完整路径。针对其他的操作系统，我们只需要知道用户的主文件夹以及文件名，就可以得到日志文件的完整路径。

我们使用 `os.path.join()` 函数连接三部分作为一个字符串，保存日志文件的完整路径。之所以使用函数做字符串连接而不是采用字符串 `+` 操作，是因为我们要确保这个操作可以在所有的操作系统环境下运行。注意：我们在这里使用的 `join()` 方法是 `os` 模块的一部分，它与我们在本书的其他地方使用的字符串方法 `join()` 不同。

我们可以配置 `logging` 模块把所有的信息用特定的格式写到我们指定的文件中。

最后，我们可以指定输出信息的属性，比如调试、提示、警告或者致命错误。一旦程序运行，我们可以通过查看这个文件了解我们程序的运行情况，即使程序没有向用户输出信息。

## Module of the Week 系列

Python 标准库还有很多有用的模块，比如[调试](http://docs.python.org/3/library/pdb.html),
[处理命令行参数](http://docs.python.org/3/library/argparse.html), [正则表达式](http://docs.python.org/3/library/re.html)等等。

进一步学习 Python 标准库的最佳方法，推荐大家阅读Doug Hellmann的[Python Module of the Week](http://pymotw.com/3/contents.html)系列，也可以在Amazon[购买](http://amzn.com/0321767349)纸质的书籍，当然你也可以直接阅读[Python官方文档](http://docs.python.org/3/)。

## 总结

我们学习了 Python 标准库的一些模块，强烈推荐大家快速浏览一下[Python标准库官方文档](http://docs.python.org/3/library/)，以获得所有可以使用的模块。

接下来，我们探讨一下 Python 语言其他方面的事情，这样可以让我们这本教程更加完整。

--------------------------------------------------

### 继续阅读[更多](more.md)
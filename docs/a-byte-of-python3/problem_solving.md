# 解决问题

我们已经探索过了Python语言的各种部分，现在我们通过设计和编写一个做有用事情的程序，看一看如何将所有这些组合在一起，学习如何自己编写一个Python脚本可以实现这个想法。

## 问题

我们想要解决的问题是：

> 我需要一个为我所有重要的程序创建备份的一个程序。

尽管这是一个简单的问题，但是我们没有着手解决这个问题的足够的信息。多一点的分析是必需的，例如，我们如何指定哪一个文件需要备份？他们是怎样存储的？

在得当的问题分析后，我们设计我们的程序。我们为程序如何工作列一个列表，在本例中，我创建了我希望它如何工作的以下列表。如果你做这个设计，你可能不会拿出同样的分析，因为每个人都有自己做事的方式，这是非常好的。

* 在列表中指出需要备份的文件和目录。
* 备份必须存储在一个主备份目录中。
* 备份的文件压缩到一个压缩文件中。
* 压缩文件的名称是当前的日期和时间。
* 在标准的 Linux/Unix 发行版上，我们默认使用标准的zip命令。注意，只要它有一个命令行，你可以使用任何你想要归档的命令。

，Windows用户可以从GnuWin32项目页 安装，并向你的系统环境变量 PATH追加C:\Program Files\GnuWin32\bin，这和为识别Python命令我们所做的类似

> **Windows用户**
> 
> Windows用户可以[安装](http://gnuwin32.sourceforge.net/downlinks/zip.php)在[GnuWin32项目主页](http://gnuwin32.sourceforge.net/packages/zip.htm)安装 `zip`命令并且将`C:\Program Files\GnuWin32\bin`添加到你的环境变量`PATH`中，就好像我们配置python命令行一样。

## 解决方案

由于我们的程序的设计现在相当稳定，我们可以写实现解决方案的代码。

保存为backup_ver1.py:

```python
import os
import time

# 1. 在列表中指出需要备份的文件和目录。
# 在Windows中的例子:
# source = ['"C:\\My Documents"', 'C:\\Code']
# 在Mac OS X和Linux中的列子:
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意我们在有空格的名字的字符串内不得不使用双引号。

# 2. 备份必须存储在一个主备份目录中。
# 在Windows中的例子:
# target_dir = 'E:\\Backup'
# 在Mac OS X和Linux中的例子:
target_dir = 'E:\\Backup' 
# 记住把它改为你要使用的目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 压缩文件的名称是当前的日期和时间。
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目录不存在就创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 5. 我们使用zip命令把文件压缩到一个压缩文件中
zip_command = "zip -qr {0} {1}".format(target, 
                                       ' '.join(source))

# 运行备份
print("Zip命令为:")
print(zip_command)
print("运行:")
if os.system(zip_command) == 0:
    print('成功备份到', target)
else:
    print('备份失败')
```

输出:

```
$ python backup_ver1.py
Zip命令为:
zip -r /Users/swa/backup/20140328084844.zip /Users/swa/notes
运行:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
成功备份到 E:\Backup\20080702185040.zip
```

现在，我们是在测试我们的程序能否正常工作的*测试*阶段。如果它不像预期的那样,则我们必须*调试*我们的程序，也就是从程序中去掉*bug*(错误)。

如果上面的程序不为你工作，将打印出来的`Zip命令为:`下面那一行拷贝一下，然后在shell(GNU/Linux和Mac OS X中)/`cmd`(Windows中)里面粘贴，看看有哪些报错，然后尝试修复它。如果这个命令失败,检查压缩命令手册，是什么可能是错的。如果这个命令成功，然后检查Python程序是否和上面的程序完全匹配。

**它是如何工作的：**

你会注意到，我们是如何以一个循序渐进的方式将我们的*设计*转换成*代码*的。

我们通过先导入和使用`os`和`time`模块，然后，我们在`source`清单中指定要备份的文件和目录，目标目录存储在变量`target_dir`中，这是我们要存储的所有的备份文件的地方，我们将要创建的压缩文件的名称是使用 `time.strftime()` 函数由当前日期和时间生成的。它也包含 `.zip`扩展名，将存储在`target_dir`目录中。

注意，变量`os.sep`的使用--目录的分隔符依你的操作系统而定，在GNU/Linux和Unix中是`'/'`，在Windows中是`'\\'`，在Mac OS中是`':'`。使用`os.sep`而不是直接使用这些字符将使我们的程序更具可移植性，在所有这些系统上都能工作。

`time.strftime()`函数获取一个技术参数，像在上面的程序中我们已经使用过的。`%Y`参数将被替换为带着世纪的年份数字。`%m`参数将被一个位于`01`到`12`的数字替换，如此等等。这种参数的完整列表可[Python参考手册](http://docs.python.org/3/library/time.html#time.strftime)中找到。

我们创建目标文件的名称zip文件使用了加法操作符连接字符串，它将两个字符串连接在了一起，并返回一个新的字符串。然后,我们创建一个包含我们要执行的命令的字符串`zip_command`。你可以通过在shell(GNU/Linux终端或DOS提示符)运行来检查这个命令的工作。

我们使用的`zip`命令有一些选项和参数。`-q`选项用于表明zip命令应该**quietly(默默地)**工作，`-r`选项指定zip命令应该**recursively(递归地)**工作，即它应该包括所有的子目录和文件。这两个选项组合在一起可缩写为`-qr`。要创建的压缩文件名后的选项后面紧跟要备份的文件和目录列表，我们使用字符串的`join`方法，这种方法我们已经知道如何使用，将`source`列表转换成一个字符串。

然后，我们终于使用`os.system`函数*运行*命令。os.system函数运行命令就仿佛在系统上也就是shell上运行它，如果命令运行成功，它返回`0`，否则返回一个错误号。

根据命令的结果，我们打印相应的消息，备份失败或成功。

就是这样，我们已经创建了一个备份我们重要文件的一个脚本!

> **Windows用户应注意**
>
> 您还可以使用原始字符串，而不是双反斜杠转义序列，例如，使用`'C:\\Documents'`或`r'C:\Documents'`。然而，*不要*使用`'C:\Documents'`，因为你最终用一个未知的转义序列`\D`。

现在，我们有一个能够工作的备份脚本，当我们想要备份文件时，我们可以用它。这被称为软件的*操作*阶段或*部署*阶段。

上面的程序正常工作，但(通常)第一个程序不会像你期望的那么样工作。例如，如果没有正确地设计程序或当键入代码时如果你犯了一个错误等，可能出现问题。相应地，你将不得不回到设计阶段或你需要调试您的程序。

## 第二版

第一个版本的脚本工作了。然而，我们还可以做一些改进，以便每天工作得更好。这被称为软件的维护阶段。

我觉得有用的改进之一是有一个更好的文件命名机制——在一个目录中，使用时间作为文件的名称，使用当前日期作为主备份目录中的一个目录。第一个优势是，你的备份以分层以方式存储，因此它更容易管理。第二个优势是，文件名短得多。第三个优势是单独的目录将帮助你检查每天是否创建了一个备份，如果某一天你备份了，将会创建一个目录。

保存为 backup_ver2.py:

```
import os
import time

# 1. 在列表中指出需要备份的文件和目录。
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意，因为名字字符串中有空格，我们不得不使用双引号。

# 2. 备份必须存储在一个主备份目录中。
target_dir = 'E:\\Backup' # 记住把它改为你要使用的目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 当前日期是主备份目录中子目录的名字
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间是压缩文件的名字
now = time.strftime('%H%M%S')

# 如果子目录不存在，创建它
if not os.path.exists(today):
    os.mkdir(today) # 建立目录
    print('成功创建目录', today)

# 压缩文件的名字
target = today + os.sep + now + '.zip'

# 5. 我们使用zip命令把文件压缩到一个压缩文件中
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# 运行备份
if os.system(zip_command) == 0:
    print('成功备份到', target)
else:
    print('备份失败')
```

输出：

```
D:> python backup_ver2.py
成功创建目录 E:\Backup\20080702
成功备份到 E:\Backup\20080702\202311.zip

D:> python backup_ver2.py
成功备份到 E:\Backup\20080702\202325.zip
```

它是如何工作的:

大部分程序还保留了原样，变化是，我们使用os.path.exists函数检查在主备份目录中是否存在以当前日期为名字的目录，如果不存在，我们使用os.mkdir函数创建它。

## 第三版

当我们做一些备份时，第二版工作起来很好了。但当有许多备份时，我发现区分为什么备份是很困难的。例如，对一个程序或描述做一些重要的改变，然后我想知道这些变化与压缩文件的名字有什么联系。这个可以通过为压缩文件的名字附加上一个用户提供的注释而轻易实现。

注意
> 下面的程序不工作，所以不要惊慌，请继续，因为在这里有一个教训。
保存为 backup_ver3.py:

```
import os
import time

# 1.  在列表中指出需要备份的文件和目录。
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意，因为名字字符串中有空格，我们不得不使用双引号。

# 2. 备份必须存储在一个主备份目录中。
target_dir = 'E:\\Backup' # 记住把它改为你要使用的目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 当前日期是主备份目录中子目录的名字
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间是压缩文件的名字
now = time.strftime('%H%M%S')

# 为创建一个压缩文件的名字从用户取得一个注释
comment = input('Enter a comment --> ')
if len(comment) == 0: # 检查是否输入注释
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +
        comment.replace(' ', '_') + '.zip'

# 如果子目录不存在，创建它
if not os.path.exists(today):
    os.mkdir(today) # 建立目录
    print('成功创建目录', today)

# 5. 我们使用zip命令把文件压缩到一个压缩文件中
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# 运行备份
if os.system(zip_command) == 0:
    print('成功备份到', target)
else:
    print('备份失败')
```

输出：

```
D:> python backup_ver3.py
  File "backup_ver3.py", line 25
    target = today + os.sep + now + '_' +
                                        ^
SyntaxError: invalid syntax
```

这怎么（不）工作：

**这个程序不工作！**Python说有语法错误这意味着脚本不满足Python预计的结构。当我们观察Python给出的错误，它还告诉我们它检测到错误的地方。所以我们从那一行开始调试我们的程序。

在仔细观察后，我们发现单一的逻辑行被分成两个物理行，但我们没有指定这两个物理行属于同一个逻辑行。基本上，Python发现在那个逻辑行添加操作符(+)没有任何操作对象，因此不知道如何继续。记住，我们可以通过在物理行的结束位置使用反斜杠指定当前行与下一物理行是连续的。所以，我们要改正我们的程序。我们找到错误时的这样修正叫做修复bug。

## 第四版

保存为 backup_ver4.py:

```
import os
import time

# 1. 在列表中指出需要备份的文件和目录。
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意，因为名字字符串中有空格，我们不得不使用双引号。

# 2. 备份必须存储在一个主备份目录中。
target_dir = 'E:\\Backup' #记住把它改为你要使用的目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 当前日期是主备份目录中子目录的名字
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间是压缩文件的名字
now = time.strftime('%H%M%S')

# 为创建一个压缩文件的名字从用户取得一个注释
comment = input('输入注释--> ')
if len(comment) == 0: # 检查是否输入注释
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# 如果子目录不存在，创建它
if not os.path.exists(today):
    os.mkdir(today) #  建立目录
    print('成功创建目录', today)

# 5. 我们使用zip命令把文件压缩到一个压缩文件中
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# 运行备份
if os.system(zip_command) == 0:
    print('成功备份到 ', target)
else:
    print('备份失败')
```

输出：

```
D:> python3 backup_ver4.py
输入注释--> added new examples
成功备份到 E:\Backup\20080702\202836_added_new_examples.zip

D:> python3 backup_ver4.py
输入注释-->
成功备份到 E:\Backup\20080702\202839.zip
```

它是如何工作的：

这个程序现在工作了！让我们仔细检查第三版的实际增强，我们使用input函数获取 用户的注解，然后通过使用len函数找到输入的长度检查用户确实输入了一些东西。如果用户只是按enter（回车键），没有输入任何东西(也许这只是一个常规备份或没有特殊的改变)，那么，我们按照我们之前所做的处理。

然而，如果提供了一个注释，那么，它将附加到压缩文档名字中、 .zip扩展名前。请注意，我们将注释中的空格用开线正在取代空间在评论中用下划线——这是因为管理没有空格的文件名容易得多。

## 更细化

第四版对于大多数用户来说是一个令人满意的工作脚本，但总有改进的余地。例如，您可以为程序包括一个冗长级别，在那里你可以指定一个-v选项，从而使你的程序变得更加健谈。

另一个可能的优化处理是将允许额外的文件和目录被传递给该脚本的命令行。我们可从sys.argv列表得到这些文件名，我们可以使用list类提供的extend方法将它们添加到我们的source列表中。

最重要的改进是不使用的创建文档的os.system 方式，而是使用转而使用内建的 zipfile 或 tarfile模块创建文档。他们是标准库的一部分，在你的计算机上已经为您提供使用没有外部依赖的压缩程序。

然而，在上面的例子中，纯粹是为教学的目的，我一直使用 os.system的方式创建一个备份，这样的例子对每个人的理解足够简单，但不是真正足够的有效。

你能使用[zipfile(压缩文件)](http://docs.python.org/3/library/zipfile.html)模块，而不是os.system调用尝试写第五版吗？

## 软件开发过程

我们已经经历了编写一个软件过程中的各种阶段。这些阶段可以概括如下：

1. 什么 (分析)
2. 怎样 (设计)
3. 做 (实现)
4. 测试 (测试和调试)
5. 使用 (操作和部署)
6. 维护 (优化)
编写程序的推荐方法是我们创建备份脚本的过程：做了分析和设计，开始实现用一个简单的版本，测试和调试它，来确保它能按预期工作。现在，添加你想要的任何功能，继续重复需要次数的做－试验循环。记住，**软件是在成长，而不是建立**。

## 小结

我们已经看到了如何创建我们自己的Python程序/脚本和编写这种程序的不同阶段。你可能会发现创建你自己的程序就像我们在这一章做的是有用的，以便你熟悉Python以及解决问题。

接下来，我们将讨论面向对象编程。 


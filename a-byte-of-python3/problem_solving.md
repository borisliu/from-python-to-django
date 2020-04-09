# 实战案例

我们已经了解了Python语言的各个方面，现在我们要通过设计和编写一个实用的程序，看一看如何将所有这些组合在一起。我们要学习如何自己编写一个Python脚本实现这个想法。

## 问题

我们想要解决的问题是：

> 我需要一个为我所有重要的程序创建备份的一个程序。

尽管这是一个简单的问题，但是我们没有着手解决这个问题的足够的信息。多一点的**分析**是必需的，例如，我们如何指定**哪一个**文件需要备份？他们是**怎样**存储的？存储在**什么位置**？

当我们完成问题的分析之后，我们要开始**设计**我们的程序。我们为程序如何工作列了一个清单。在本例中，我创建了**我**希望它如何工作的以下清单。如果你来做这个设计，你可能会拿出不一样的分析，因为每个人都有自己做事的方式，事实本该如此。

* 在列表中指出需要备份的文件和目录。
* 备份必须存储在一个主备份目录中。
* 备份的文件压缩到一个zip文件中。
* zip文件的名称是当前的日期和时间。
* 在标准的 Linux/Unix 发行版上，我们默认使用标准的`zip`命令。注意，只要它有一个命令行，你可以使用任何你想要归档的命令。

> **Windows用户**
> 
> Windows用户可以在[GnuWin32项目主页](http://gnuwin32.sourceforge.net/packages/zip.htm)[下载](http://gnuwin32.sourceforge.net/downlinks/zip.php)并安装 `zip`命令，记得要将`C:\Program Files (x86)\GnuWin32\bin`添加到你的环境变量`PATH`中，就好像我们[配置python命令行](installation.md)一样。

## 解决方案

由于我们程序的设计已经完成，现在可以编写**实现**解决方案的代码。

保存为backup_ver1.py:

```python
import os
import time

# 1. 在列表中指出需要备份的文件和目录。
# 在Mac OS X和Linux中的列子:
# source = ['/Users/swa/notes']
# 在Windows中的例子:
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意我们在有空格的名字的字符串内必须使用双引号。
# 我们也可以使用原始字符串[r'C:\My Documents']。

# 2. 备份必须存储在一个主备份目录中。
# 在Mac OS X和Linux中的例子:
# target_dir = '/Users/swa/backup'
# 在Windows中的例子:
target_dir = 'D:\\Backup' 
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

```shell
C:\> python backup_ver1.py
Zip命令为:
zip -qr D:\Backup\20200407113117.zip "C:\My Documents" C:\Code
运行:
成功备份到 D:\Backup\20200407113117.zip
```

现在，我们处于**测试**阶段，也就是说我们要测试一下我们的程序能否正常工作。如果它不像预期的那样运行，我们就必须**调试**我们的程序，也就是从程序中去掉**bug**（错误）。

如果上面的程序不为你工作，将打印出来的`Zip命令为:`下面那一行拷贝一下，然后在`cmd`(Windows中)/shell(GNU/Linux和Mac OS X中)里面粘贴，看看有哪些报错，然后尝试修复它。如果这个命令无法执行，查阅一下压缩命令手册，看看错在哪里。如果这个命令成功执行，那么就检查Python程序是否和上面的程序完全匹配。

**它是如何工作的：**

你会注意到，我们是如何以一个循序渐进的方式将我们的**设计**转换成**编码**的。

我们首先导入`os`和`time`模块，然后，我们在`source`清单中指定要备份的文件和路径，目标路径存储在变量`target_dir`中，这是我们要存储所有备份文件的地方。我们将要创建的压缩文件名是使用 `time.strftime()` 函数由当前日期和时间生成的。它也包含`.zip`扩展名，存储在`target_dir`目录中。

注意，变量`os.sep`的使用--目录的分隔符根据你的操作系统而定：在GNU/Linux、Unix和MacOS中是`'/'`，在Windows中是`'\\'`。使用`os.sep`而不是直接使用这些字符将使我们的程序更具可移植性，在所有这些系统上都能工作。

`time.strftime()`函数需要一个参数指定字符串的规格，就像在上面的程序中我们已经使用过的那样。`%Y`参数将被替换为带着世纪的年份数字（如2020）。`%m`参数将被一个位于`01`到`12`的数字替换，以此类推。这些参数的完整列表可以在[Python参考手册](http://docs.python.org/3/library/time.html#time.strftime)中找到。

我们创建的目标zip文件名使用了加法运算符连接字符串，它将两个字符串**连接**在了一起，并返回一个新的字符串。然后，我们创建一个包含我们要执行的命令的字符串`zip_command`。你可以通过在shell(GNU/Linux终端或DOS提示符)运行来验证这个命令是否可以正常工作。

我们使用的`zip`命令有一些参数。`-q`选项用于表明zip命令应该**quietly(默默地)**工作。`-r`选项指定zip命令应该**recursively(递归地)**工作，即它应该包括所有的子目录和文件。这两个选项组合在一起可缩写为`-qr`。要创建的压缩文件名后的参数后面紧跟要备份的文件和目录列表。在程序中我们使用字符串的`join`函数，这个函数`source`列表转换成一个字符串。

最后我们使用`os.system`函数**运行**命令，就仿佛在**系统**上（也就是shell上）运行它，如果命令运行成功，它返回`0`，否则返回一个错误号。

根据命令的结果，我们打印相应的消息，备份失败或成功。

就是这样，我们已经创建了一个备份我们重要文件的一个脚本!

> **Windows用户应注意**
>
> 您还可以使用原始字符串，而不是双反斜杠转义字符，例如，使用`'C:\\Documents'`或`r'C:\Documents'`。然而，**不要**使用`'C:\Documents'`，因为你最终用一个未知的转义字符`\D`。

现在，我们有一个能够工作的备份脚本，当我们想要备份文件时，我们可以用它。这被称为软件的**运行**阶段或**部署**阶段。

上面的程序正常工作，但(通常)第一个程序不会像你期望的那样工作。例如，如果没有正确地设计程序或当键入代码时如果你犯了一个错误等，可能出现问题。相应地，你将不得不回到设计阶段或你需要调试你的程序。

## 第二版

第一个版本的脚本工作了。然而，我们还可以做一些改进，以便满足我们的日常需求。这被称为软件的**维护**阶段。

我觉得有用的改进之一是有一个更好的文件命名机制——在一个目录中，使用**时间**作为文件的名称，使用当前**日期**作为主备份目录中的一个目录。这样做的第一个优点是备份文件分层存放，便于管理管理；第二个优点是文件名更短了；第三个优点是每天独立的目录让你很容易就能知道今天是否进行了备份。因为只有完成了今天的备份，目录才会被建立。

保存为 backup_ver2.py:

```python
import os
import time

# 1. 在列表中指出需要备份的文件和目录。
# 在Mac OS X和Linux中的列子:
# source = ['/Users/swa/notes']
# 在Windows中的例子:
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意我们在有空格的名字的字符串内必须使用双引号。
# 我们也可以使用原始字符串[r'C:\My Documents']。

# 2. 备份必须存储在一个主备份目录中。
# 在Mac OS X和Linux中的例子:
# target_dir = '/Users/swa/backup'
# 在Windows中的例子:
target_dir = 'D:\\Backup'
# 记住把它改为你要使用的目录

# 如果目录不存在就创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 在主备份目录中创建一个子目录，名字是当前的日期。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# zip文件的名字是当前的时间。
now = time.strftime('%H%M%S')

# zip文件的完整路径
target = today + os.sep + now + '.zip'

# 如果子目录不存在就创建它
if not os.path.exists(today):
    os.mkdir(today)
    print('成功创建子目录：', today)

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

输出：

```shell
C:\> python backup_ver2.py
成功创建子目录： D:\Backup\20200409
Zip命令为:
zip -qr D:\Backup\20200409\151018.zip "C:\My Documents" C:\Code
运行:
成功备份到 D:\Backup\20200409\151018.zip
```

**它是如何工作的:**

第二版的大部分代码都是一样的。主要的改进之处是使用`os.path.exists`函数检查主备份目录下有没有以当前日期命名的文件夹，如果没有，则通过`os.mkdir` 函数创建一个。

## 第三版

当我们做一些备份时，第二版工作起来很好了。但当有许多备份时，我发现区分为什么备份是很困难的。例如，对一个程序或描述做一些重要的改变，然后我想知道这些变化与压缩文件的名字有什么联系。这个可以通过为压缩文件的名字附加上一个用户提供的注释而轻易实现。

注意：下面的程序不工作，所以不要惊慌，请继续，因为在这里有一个教训。
保存为 backup_ver3.py:

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

# 如果目录不存在就创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 在主备份目录中创建一个子目录，名字是当前的日期。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# zip文件的名字是当前的时间。
now = time.strftime('%H%M%S')

# 提示用户输入zip文件名中附加的注释
comment = input('输入注释 --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + 
        comment.replace(' ', '_') + '.zip'

# 如果子目录不存在就创建它
if not os.path.exists(today):
    os.mkdir(today)
    print('成功创建子目录：', today)

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

输出：

```
$ python backup_ver3.py
  File "backup_ver3.py", line 25
    target = today + os.sep + now + '_' +
                                        ^
SyntaxError: invalid syntax
```

**这怎么（不）工作：**

**这个程序不工作！**Python说有语法错误这意味着脚本不满足Python预计的结构。当我们观察Python给出的错误，它还告诉我们它检测到错误的地方。所以我们从那一行开始调试我们的程序。

在仔细观察后，我们发现单一的逻辑行被分成两个物理行，但我们没有指定这两个物理行属于同一个逻辑行。基本上，Python发现在那个逻辑行添加操作符(+)没有任何操作对象，因此不知道如何继续。记住，我们可以通过在物理行的结束位置使用反斜杠指定当前行与下一物理行是连续的。所以，我们要改正我们的程序。我们找到错误时的这样修正叫做修复bug。

## 第四版

保存为 backup_ver4.py:

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

# 如果目录不存在就创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 在主备份目录中创建一个子目录，名字是当前的日期。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# zip文件的名字是当前的时间。
now = time.strftime('%H%M%S')

# 提示用户输入zip文件名中附加的注释
comment = input('输入注释 --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# 如果子目录不存在就创建它
if not os.path.exists(today):
    os.mkdir(today)
    print('成功创建子目录：', today)

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

输出：

```
$ python3 backup_ver4.py
输入注释--> added new examples
成功备份到 E:\Backup\20080702\202836_added_new_examples.zip

$ python3 backup_ver4.py
输入注释-->
成功备份到 E:\Backup\20080702\202839.zip
```

**它是如何工作的：**

这个程序现在工作了！让我们仔细检查第三版的实际增强，我们使用`input`函数获取 用户的注解，然后通过使用`len`函数找到输入的长度检查用户确实输入了一些东西。如果用户只是按`enter`（回车键），没有输入任何东西(也许这只是一个常规备份或没有特殊的改变)，那么，我们按照我们之前所做的处理。

然而，如果提供了一个注释，那么，它将附加到压缩文档名字中、 `.zip`扩展名前。请注意，我们将注释中的空格用开线正在取代空间在评论中用下划线——这是因为管理没有空格的文件名容易得多。

## 更细化

第四版对于大多数用户来说是一个令人满意的工作脚本，但总有改进的余地。例如，您可以为程序包括一个冗长级别，在那里你可以指定一个`-v`选项，从而使你的程序变得更加健谈。

另一个可能的优化处理是将允许额外的文件和目录被传递给该脚本的命令行。我们可从`sys.argv`列表得到这些文件名，我们可以使用`list`类提供的`extend`方法将它们添加到我们的`source`列表中。

最重要的改进是不使用的创建文档的`os.system` 方式，而是使用转而使用内建的 [zipfile](http://docs.python.org/3/library/zipfile.html) 或 [tarfile](http://docs.python.org/3/library/tarfile.html)模块创建文档。他们是标准库的一部分，在你的计算机上已经为您提供使用没有外部依赖的压缩程序。

然而，在上面的例子中，纯粹是为教学的目的，我一直使用 `os.system`的方式创建一个备份，这样的例子对每个人的理解足够简单，但不是真正足够的有效。

你能使用[zipfile](http://docs.python.org/3/library/zipfile.html)模块，而不是`os.system`调用尝试写第五版吗？

## 软件开发过程

我们已经经历了编写一个软件过程中的各种阶段。这些阶段可以概括如下：

1. 什么 (分析)
2. 怎样 (设计)
3. 做 (实现)
4. 测试 (测试和调试)
5. 使用 (操作和部署)
6. 维护 (优化)
编写程序的推荐方法是我们创建备份脚本的过程：做了分析和设计，开始实现用一个简单的版本，测试和调试它，来确保它能按预期工作。现在，添加你想要的任何功能，继续重复需要次数的做－试验循环。

记住：

> 软件是在成长，而不是建立。
> -- [Bill de hÓra](http://97things.oreilly.com/wiki/index.php/Great_software_is_not_built,_it_is_grown)

## 小结

我们已经看到了如何创建我们自己的Python程序/脚本和编写这种程序的不同阶段。你可能会发现创建你自己的程序就像我们在这一章做的是有用的，以便你熟悉Python以及解决问题。

接下来，我们将讨论面向对象编程。 

--------------------------------------------------

### 继续阅读[面向对象编程](oop.md)
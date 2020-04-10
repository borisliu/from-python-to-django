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

第二版解决了要做多次备份的问题。但当有许多备份时，我发现区分为什么备份是很困难的。例如，我们对一个程序或描述做一些重要的改变，然后我想把这些变化与压缩文件的名字联系起来。这个很容易实现，只要我们让用户提供一个注释，然后把这个注释附加到压缩文件的名字上。

警告：下面的版本不能正常使用，但无需担心，跟着教程往下走吧。

保存为 backup_ver3.py:

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

```shell
C:\> python backup_ver3.py
  File "backup_ver3.py", line 35
    target = today + os.sep + now + '_' + 
                                         ^
SyntaxError: invalid syntax
```

**它是如何（不）工作的：**

**这个程序不工作！**Python报告了一个语法错误，表示脚本中存在Python无法识别的语法结构。当我们审视Python给出的错误提示时，就会发现它已经给出错误发生的地方。所以我们从那一行开始**调试**我们的程序。

在仔细观察后，我们发现单一的逻辑行被分成两个物理行，但我们没有指定这两个物理行属于同一个逻辑行。实际上，Python发现在那个逻辑行末尾有一个加号运算符(`+`)，但没有任何操作对象，因此不知道如何继续。记住，如果我们要指定一个逻辑行需要与下一个逻辑行是连续的，我们可以在第一行的末尾添加一个反斜杠。所以，我们要修订我们的程序。我们找到错误并改正它叫做**修复bug**。

## 第四版

保存为 backup_ver4.py:

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

```shell
C:\> python3 backup_ver4.py
输入注释 --> added new examples
成功创建子目录： D:\Backup\20200410
Zip命令为:
zip -qr D:\Backup\20200410\173214_added_new_examples.zip "C:\My Documents" C:\Code
运行:
成功备份到 D:\Backup\20200410\173214_added_new_examples.zip
```

**它是如何工作的：**

这个程序现在工作了！让我们回顾一下我们在第三版中做了什么实质性的改进：我们用`input`函数获得用户输入的注释，并通过`len`函数获得用户输入的长度，以确定用户真的输入了注释。如果用户什么都没有输入，只是按下了`enter`键，可能这只是一次日常的备份、没什么特别的，那么我们就像之前一样产生文件名。

而当用户输入了注释时，注释会被用作 zip 存档的文件名，放在`.zip`扩展名之前。请注意，我们把文件名中的空格替换为下划线了，这是因为以后处理没有空格的文件名更简单。

## 更多改进

第四版的程序对大多数用户来说足够了，但程序总有改进的余地。举个例子：你可以通过指定`-v`选项使zip命令输出更丰富的信息，让你的程序更有交互性；或者增加一个`-q`选项，让程序能**静默**运行。

另一个可能的改进是允许通过命令行指定额外需要备份的文件和目录。我们可以通过`sys.argv`列表获得这些名字，然后用`list`类的`extend`方法把他们加到`source`列表里。

最重要的改进可能是不使用`os.system`来创建备份，而用内置的 [zipfile](http://docs.python.org/3/library/zipfile.html) 或 [tarfile](http://docs.python.org/3/library/tarfile.html) 模块来创建备份。它们是标准库的一部分，你可以直接使用它们，而不需要额外的 zip 程序依赖。

我在上面的示例程序中使用`os.system`纯粹是出于教学需要，因为这样示例足够简单，每个人都能理解，同时也足够真实有用。

你可以尝试编写使用[zipfile](http://docs.python.org/3/library/zipfile.html)模块而不是`os.system`调用的第五版程序吗？

## 软件开发过程

现在我们已经经历了编写软件的不同**阶段**。这些阶段可以概括成以下环节：

1. 需求 (分析需求)
2. 设计 (确定方法)
3. 编码 (编写代码)
4. 测试 (测试和调试)
5. 运行 (运行和部署)
6. 维护 (优化与重构)

我们推荐参考上面编写备份脚本的过程来编写你的程序：一开始进行需求分析和系统设计，然后实现一个简单的版本，对它进行测试，有bug就进行调试。接着运行它，确保它能像设计的那样正常工作。再增加你想要的新功能，并继续重复编码 - 测试 - 运行的循环，直到软件实现预期的功能。

记住：

> 好的软件是改出来的，不是做出来的
> -- [Bill de hÓra](http://97things.oreilly.com/wiki/index.php/Great_software_is_not_built,_it_is_grown)

## 小结

我们已经学会了如何编写自己的 Python 脚本程序，并知道了编写程序的不同阶段。你可能已经发现使用本章的方法编写程序非常方便，你也因此能更加熟练的使用 Python 去解决问题。

接下来我们会讨论面向对象编程。

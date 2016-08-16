# 第一步
=======

现在,我们将看到在Python中如何运行一个传统的“Hello World”程序。这将教你如何写、保存和运行Python程序。

使用Python运行你的程序有两种方法——使用交互式解释器提示符或使用一个源文件。现在,我们将看到如何使用这两种方法。

## 使用解释器提示符

在您的操作系统中打开终端(如前面[安装](a-byte-of-python3/install.md)所述),然后，输入`python3`按回车键，打开Python提示符。

一旦你启动python 3,您应该看到'>>>”,这被称为_Python解释器提示符_，你可以开始输入Python程序。

在Python解释器提示符下，输入

```python
print("Hello World")
```

然后按回车键。您应该看到输出了单词“Hello World”。

当使用一个Mac OS X计算机，下面是你将看到的一个例子。Python软件的细节会根据你的电脑不同而有所不同，但从提示符(即从“>>>”开始)与操作系统无关，应该是相同。

```python
> python3
Python 3.5.2 (default, Jan 14 2016, 06:54:11)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
```

注意,Python让你的代码行立即输出了!你刚才输入的是一个Python_语句_。我们使用`print`输出(不出所料)你提供给它的任何值。在这里,我们提供的是文本“Hello World”,并立即打印到屏幕上。

### 如何退出解释器提示符

如果你正在使用一个Linux或Unix shell,您可以通过按下`[ctrl - d]`或输入`exit()`(注意:记得包含括号,`()`)，然后输入回车键。

如果您使用的是Windows命令行提示符,按`[ctrl - z]`键再按回车键，退出解释器提示符。

## 选择一个编辑器

我们不能在每次想要运行一些东西的时候都要在解释器提示符下输入我们的程序，所以我们必须把它们保存为文件，这样我们可以任意次地运行我们的程序。

要创建我们的Python源文件,我们需要一个可以输入并保存它们的编辑软件。一个优秀的程序员的编辑器将使你写源代码文件的生活更容易。因此，选择一个编辑器确实至关重要。你必须选择一个编辑器，就像你选择要买的汽车一样。一个好的编辑器会帮助您很容易地编写Python程序，（就像一辆车可以让你）以一个更快和更安全的方式，让你的旅程更舒适，并且可以帮助你实现你的目标。

一个非常基本的需求是_语法高亮显示_，分别以不同的彩色显示你的Python程序所有的不同部分，以便您可以看到你的程序且使其运行可视化。

如果你不知道从哪里开始，我推荐可以在Windows、Mac OS X和GNU/Linux上使用的[Visual Studio Code](https://code.visualstudio.com/)(简称VSCode)免费软件与Python插件(ext install python)。

如果您使用的是Windows，*不要使用记事本*——这是一个糟糕的选择，因为它不做语法高亮显示，而且更重要的是它不支持文字的缩进——之后我们在我们的例子中会看到，缩进是非常重要的。好的编辑器如Komodo Edit会自动地做到这一点。

如果你是一名有经验的程序员，那么你一定已经使用[Vim](http://www.vim.org/)或[Emacs](http://www.gnu.org/software/emacs/)了。不用说，这是两个最强大的编辑器，使用它们来写你的Python程序，你会从中受益。就我自己而言，在我的大多数项目,甚至写一[整本书都在用Vim](http://www.swaroopch.com/notes/vim)。

从长远来看Vim或者Emacs是非常有用的，如果你愿意花时间去学习，那么我强烈建议你使用它们。然而,正如我之前提到的,初学者可以从PyCharm开始学习Python而不是编辑器。

再次重申，请选择一个适当的编辑器，它可以使编写Python程序更有趣和更容易。

## VSCode

[Visual Studio Code](https://code.visualstudio.com/)是一个免费的集成开发环境（IDE），你可以用它开发Python程序。

下载安装之后，在菜单中选择“查看”->“扩展”，然后输入`python`，选择由`Don Jayamanne`开发的Python扩展安装即可。

<!-- TODO: 增加控件的截图 -->

在VSCode中，新建项目就是新建一个文件夹，你可以使用操作系统的资源管理器新建文件夹，然后在当前文件夹下使用命令行`code .`启动VSCode。也可以在VSCode中使用“文件”->"打开...“打开这个文件夹。

打开文件夹之后，在左侧的资源管理器中右键单击，在弹出菜单中选择“新建文件”，然后输入`helloworld.py`，点击回车即可。

输入以下代码：

```python
print("hello world!")
```

点击`[Ctrl+S]`保存文件之后，选择最左侧的`调试`视图，然后点击上面的绿色小三角，运行`helloworld.py`程序。此时VSCode会弹出一个列表让你选择环境，在这里选择`Python`即可。

<!-- TODO: 增加选择执行环境的截图 -->

再次点击绿色的小三角按钮，会看到程序没有立即运行，而是进入了调试状态，在中间出现了调试的对话框，点击那个绿色的小三角按钮即可运行程序，看到`hello world!`的输出。

<!-- TODO: 增加程序输出的截图 -->

之所以要再点击一次，是因为VSCode的Python插件默认的启动配置为：

```
"stopOnEntry": true,
```

可以修改为false，这样以后点击“运行”的时候就直接执行程序了。

## Vim

1. 安装[Vim](http://www.vim.org)
    * Mac OS X用户应该通过[HomeBrew](http://brew.sh/)安装`macvim`软件 。
    * Windows用户应该在[Vim网站](http://www.vim.org/download.php)下载exe安装文件。
    * GNU/Linux用户一般情况下可以直接使用`vim`。
2. 你可以安装[jedi-vim](https://github.com/davidhalter/jedi-vim)这个插件为vim增加自动完成的功能。
3. 女装对应的`jedi`python包 : `pip install -U jedi`

## Emacs

1. I安装[Emacs 24+](http://www.gnu.org/software/emacs/).
    * Mac OS X用户从[http://emacsformacosx.com](http://emacsformacosx.com)获得emacs
    * Windows用户从[http://ftp.gnu.org/gnu/emacs/windows/](http://ftp.gnu.org/gnu/emacs/windows/)下载
    * GNU/Linux用户根据不同的发行版获得对应的emacs软件，比如Debian和Ubuntu用户可以安装`emacs24`软件包
2. 安装[ELPY](https://github.com/jorgenschaefer/elpy/wiki)

## 使用一个源文件

现在让我们回到编程。每当你学习一种新的编程语言时，有一个传统，你编写和运行的第一个程序是“Hello World”程序——当你运行它时，它所做的只是说“Hello World”。正如Simon Cozens(神奇的"Beginning Perl"的作者)所说，这是“向编程神祈求帮你更好学习语言的传统咒语。”

开始你选择的编辑器，输入以下程序并将其保存为“hello.py’。

如果你使用VSCode编辑器，点击“文件”->“新建文件”,输入下行:

```
print('Hello World')
```

在VSCode编辑器，选"文件”->“保存”保存文件。

你应将文件保存在哪里？你知道位置的任何文件夹。如果你不明白这是什么意思，创建一个新文件夹，并使用该位置保存和运行你所有的Python程序:

- C:\py 在Windows上
- /tmp/py 在Linux上
- /tmp/py 在Mac OS X上

使用'mkdir'命令在命令行创建一个文件夹，例如,“mkdir /tmp/py”。

重要提示：确保你给它的文件扩展名是.py，例如，“foo.py”。

运行你的Python程序:

1. 打开一个命令行窗口。
2. **进入**你刚才保存文件的目录，例如：`cd /tmp/py`。
3. 键入`python hello.py`运行python程序，输入如下：

```
$ python hello.py
hello world
```

<!-- TODO: 增加程序输出的截图 -->

如果你得到了如上所示有输出，祝贺你!——你已经成功地运行了你的第一个Python程序。您已经成功地越过学习编程最难的部分－－开始你的第一个程序!

如果你得到了一个错误，请完全输入如上所示程序，再次运行这个程序。注意，Python是区分大小写的，即“print”并不等于“Print”——注意，前者是小写字母“p”和后者是大写字母“P”。同样，确保每一行的第一个字母之前没有空格或制表符——之后我们将明白为什么这很重要。

**它是如何工作的**

Python程序是由语句组成，在我们的第一个程序中，我们只有一个语句，在这个语句中，我们调用“print”*函数*，它只是打印文本“Hello World”。

## 获得帮助

如果您需要快速获取任何的Python函数或语句的信息，那么您可以使用内置的“help”(帮助)功能。这是非常有用的，尤其是当使用翻译提示符时，例如，运行‘help(print)”——这将显示print函数的帮助－－用于打印东西到屏幕上。

注意：按q退出帮助

类似地,您可以获得Python中几乎任何事情的信息，使用“help()”去学习更多关于使用“help”本身的信息!

如果你需要获取操作符，如“return”的帮助，那么你只需要把这些放到引号内部，如“help('return'），所以，对于我们试图要做的事情，Python并不感到困惑。

## 总结

现在，你可以自由自在地编写、保存和运行Python程序了。

既然你是一名Python用户，让我们学习一些Python概念。

--------------------------------------------------

### 继续阅读[基础](basics.md)
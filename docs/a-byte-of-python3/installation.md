# 安装

本书所描述的"Python 3"，指的是[Python 3.5.2](https://www.python.org/downloads/)或更高的版本。

## 在Windows上安装

访问[下载]https://www.python.org/downloads/最新版本。安装过程和其它基于Windows的软件类似。

警告
> 一定要选择`Add Python 3.5 to PATH`

如果想要修改安装路径，点击`Customize installation`, 再点击`Next`，键入`C:\python35`作为新的安装路径。

如果在安装的时候没有选择，那么请`添加Python环境变量`. 这和`Add Python 3.5 to PATH`效果相同。

你可以选择为所有用户安装Python Launcher，这不是特别重要的选项。Launcher用来在不同的Python版本之间进行切换。

如果你指定的安装路径不正确，你需要修正他。否则，请参考`在Windows命令行上运行Python`。

提示: 对于有经验的程序员，如果你对Docker比较熟悉，请参考[Python in Docker](https://hub.docker.com/_/python/) 和 [Docker on Windows](https://docs.docker.com/windows/).

### DOS提示符

如果你想要在Windows命名行，例如DOS提示符，使用Python，那么你需要正确设置PATH变量。

对于Windows 2000、XP、2003，点击控制面板---系统---高级---环境变量。在“系统变量”中点击PATH，选择编辑，然后在已有内容的最后部分添加;C:\Python35（请核实存在该文件夹，对于较新版本Python来说，文件夹的名字可能不同）。当然，要使用正确的目录名。

对于早期版本的Windows，打开C:\AUTOEXEC.BAT文件，添加一行“PATH=%PATH%;C:\Python35”（不含引号），然后重启系统。对于Windows NT，使用AUTOEXEC.NT文件。

对于Windows Vista:

*	点击“开始”，选择“控制面板”。
*	点击“系统”，在右侧您将看到“查看计算机基本信息”。
*	左侧是一个任务列表，其最后一项是“高级系统设置”，点击它。
*	显示“系统属性”对话框“高级”选项卡。点击右下角的“环境变量”按钮。
*	在下方标题为“系统变量”框中，滚动“Path”，点击“编辑”按钮。
*	按需修改路径。
*	重启系统。除非重启，Vista不会意识到系统路径变量的修改。

对于Windows 7/8/10:

*	在桌面上右击“计算机”，选择“属性”；或点击“开始”，选择“控制面板”---“系统和安全”---“系统”，点击左侧的“高级系统设置”，然后选择“高级”选项卡。点击底部的“环境变量”按钮，在下方的“系统变量”中找到PATH变量，选中它点击“编辑”。
*	在变量值的最后，追加;C:\Python35。
如果这个值是%SystemRoot%\system32;，它将变成%SystemRoot%\system32;C:\Python35。
*	点击“确定”完成。不需要重启。

### 在Windows命令行上运行Python

对于Windows用户，如果正确设置了PATH变量，你可以在命名行运行解释器。

要打开Windows终端，点击开始按钮，点击“运行”。在对话框输入cmd，按下回车键。

然后输入

```
python -V
```

确保没有错误。

## 在Mac OS X上安装

对于Mac OS X用户，使用[Homebrew](http://brew.sh)命令：`brew install python3`安装。

通过按Command+Space键打开终端（打开Spotlight搜索），输入`Terminal`然后回车。之后，运行

```
python3 -V
```

确保没有错误。

## 在GNU/Linux上安装

对于GNU/Linux用户，使用你的Linux发行版的包管理器来安装Python 3，例如如果你使用的是Debian & Ubuntu: `sudo apt-get update && sudo apt-get install python3`。

对于Linux用户，通过打开Terminal应用程序打开终端，或者按下Alt + F2，然后输入gnome-terminal。如果不成功，请参考文档或你所用Linux发行版的论坛。

一旦你完成安装，在shell运行python3 -V，在屏幕上你应该能够看到Python版本：

```
	$ python3 -V
	Python 3.5.2
```

提示：是shell的提示符，根据你电脑上的操作系统的设置会有所不同，因此我将使用$符号。

注意：在不同的电脑上输入信息可能会有所不同，取决于你安装的Python版本。

## 总结

现在开始，我们假设你已经在你的系统上安装好了Python 3。

接下来，我们将开始编写我们的第一个Python程序。

--------------------------------------------------

### 继续阅读[第一步](a-byte-of-python3/first_steps.md)
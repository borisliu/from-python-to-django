# 安装
=======

## 在Windows上安装

访问下载最新版本。安装过程和其它基于Windows的软件类似。

警告
> 当您提示某些“可选”组件的时候，不要不选。

### DOS提示符

如果你想要在Windows命名行，例如DOS提示符，使用Python，那么你需要正确设置PATH变量。

对于Windows 2000、XP、2003，点击控制面板---系统---高级---环境变量。在“系统变量”中点击PATH，选择编辑，然后在已有内容的最后部分添加;C:\Python33（请核实存在该文件夹，对于较新版本Python来说，文件夹的名字可能不同）。当然，要使用正确的目录名。

对于早期版本的Windows，打开C:\AUTOEXEC.BAT文件，添加一行“PATH=%PATH%;C:33”（不含引号），然后重启系统。对于Windows NT，使用AUTOEXEC.NT文件。

对于Windows Vista:

*	点击“开始”，选择“控制面板”。
*	点击“系统”，在右侧您将看到“查看计算机基本信息”。
*	左侧是一个任务列表，其最后一项是“高级系统设置”，点击它。
*	显示“系统属性”对话框“高级”选项卡。点击右下角的“环境变量”按钮。
*	在下方标题为“系统变量”框中，滚动“Path”，点击“编辑”按钮。
*	按需修改路径。
*	重启系统。除非重启，Vista不会意识到系统路径变量的修改。

对于Windows 7:

*	在桌面上右击“计算机”，选择“属性”；或点击“开始”，选择“控制面板”---“系统和安全”---“系统”，点击左侧的“高级系统设置”，然后选择“高级”选项卡。点击底部的“环境变量”按钮，在下方的“系统变量”中找到PATH变量，选中它点击“编辑”。
*	在变量值的最后，追加;C:\Python33。
如果这个值是%SystemRoot%\system32;，它将变成%SystemRoot%\system32;C:\Python33。
*	点击“确定”完成。不需要重启。

### 在Windows命令行上运行Python

对于Windows用户，如果正确设置了PATH变量你可以在命名行运行解释器。

要打开Windows终端，点击开始按钮，点击“运行”。在对话框输入cmd，按下回车键。

然后输入python3 -V，确保没有错误。

## 在Mac OS X上安装

对于Mac OS X用户，通过按Command+Space键打开终端（打开Spotlight搜索），输入Terminal然后回车。

安装Homebrew时运行：

ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
然后安装Python 3 使用

brew install python3
现在，运行python3 -V，确保没有错误。

## 在Linux上安装

对于Linux用户，通过打开Terminal应用程序打开终端，或者按下Alt + F2，然后输入gnome-terminal。如果不成功，请参考文档或你所用Linux发行版的论坛。

下一步，我们需要安装python3包。例如，在Ubuntu上，可以使用sudo apt-get install python3。请参阅文档或是你安装的Linux发行版的论坛，寻找正确的包管理器运行。

一旦你完成安装，在shell运行python3 -V，在屏幕上你应该能够看到Python版本：

```
	$ python3 -V
	Python 3.3.0
```

注意

> 是shell的提示符，根据你电脑上的操作系统的设置会有所不同，因此我将使用$符号。

新的发行版默认安装？

> 新的发行版，例如Ubuntu 12.10将Python 3作为默认版本，所以，检查一下是不是已经安装了。

## 总结

现在开始，我们假设你已经在你的系统上安装好了Python 3。

接下来，我们将开始编写我们的第一个Python 3程序。

--------------------------------------------------

### 继续阅读[第一步](a-byte-of-python3/firststep)
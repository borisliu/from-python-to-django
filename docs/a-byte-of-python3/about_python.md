# 简介
===

Python是可以称得上即简单又功能强大的少有的语言中的一种。你将会惊喜地发现，专注于问题的解决方案而不是你正在使用的编程语言的语法以及结构，是多么容易。

官方对Python的介绍：

> Python是一个易于学习的、功能强大的编程语言。它具有高效的高级数据结构和能够简单有效地实现面向对象编程。Python优美的语法和动态类型，连同解释型特性一起，使其在多个平台的许多领域都成为脚本处理以及快速应用开发的理想语言。

在下一章，我将更详细地讨论这些特性。

## 名字背后的故事

> Python语言的发明人Guido van Rossum以BBC的喜剧《Monty Python's Flying Circus》给这个语言命名。他不是特别喜欢那些为了食物而杀死动物的蛇，这些蛇会用它们长长的身体缠绕住那些动物从而勒死它们。

## Python的特点

### 简单

Python是一门简单而文字简约的语言。阅读优秀的Python程序感觉就像阅读英语，尽管是非常严格的英语。Python的这种伪代码特性是其最大强项之一，它可让你专注于解决问题的办法而不是语言本身。

### 容易学习

正如你即将看到的，Python非常容易上手。就像刚刚提到的，Python具有格外简单的语法。

### 免费开源

Python是一个FLOSS（自由/自由与开源软件）的例子。在一些简单的条款之下，你可以自由地分发这个软件的拷贝，阅读其源代码，修改它，或者将其一部分用到新的自由程序中。FLOSS是基于共享知识社区的概念，这是Python如此好的原因之一——它是由那些希望看到更好的Python的社区创建和不断改进的。

### 高级语言

当你使用Python编写程序时，你永远不需要担心低级细节，比如你的程序管理内存的使用等。

### 可移植

基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。只要你足够小心，避免使用系统相关特性，你的所有Python程序都可以不加修改地运行在这其中任意平台。

你可以在Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acorn RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE，甚至PocketPC平台上使用Python。

你甚至可以使用[Kivy](http://kivy.org)平台为iOS（iPhone、iPad）和Android创建游戏。

### 解释型

这需要一些解释。

使用编译型语言（像C或者C++）编写的程序，会由编译器使用一系列标志和选项，将源代码（如C或者C++）转换成一种电脑能够识别的语言（二进制代码，也就是0和1）。在运行程序时，链接器/载入软件将程序从硬盘复制到内存，然后开始运行。

换句话说，Python不需要编译成二进制代码。你只需从源代码直接运行程序。在内部，Python将源代码转换成一种称为字节码的中间格式，然后将其翻译你的计算机的机器语言，然后开始运行。事实上，这一切都让Python的使用更为简单，因为你不必担心程序的编译、保证恰当的库被链接和载入等等。这也使得你的Python程序更易于移植，因为你只需要复制你的Python程序到另外一台计算机，然后它就可以工作了！

### 面向对象

Python同时支持面向过程和面向对象编程。在面向过程语言中，程序围绕着过程或者函数（只不过是可重复使用的程序片段）构建。在面向对象语言中，程序围绕着对象（数据和功能的组合）构建。Python具有非常强大但是过于简洁的执行面向对象编程的方式，特别是相对于C++或者Java这种大型语言来说。

### 可扩展

如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。

### 可嵌入

你可以将Python嵌入到C/C++程序，让你的程序的用户获得“脚本化”的能力。

### 扩展库

Python标准库的确很大。它能够帮助你完成许多工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI（公共网关接口）、FTP（文件传输协议）、电子邮件、XML（可扩展标记语言）、XML-RPC（远程方法调用）、HTML（超文本标记语言）、WAV（音频格式）文件、加密、GUI（图形用户界面）以及其它系统相关的代码。记住，只要安装了Python，所有这些都能做到。这叫做Python的“遥控器”哲学。

除了标准库，还有各式各样的其它高质量库，你可以在[Python包索引](http://pypi.python.org/pypi)找到它们。

### 小结
Python的确是一个激动人心的功能强大的语言。Python那种性能和特性的恰到好处的组合让使用Python编程既有趣又简单。

## Python 3 vs 2

如果你不关心Python 2和Python 3的区别，可以跳过这一节。但是必须知道你正在使用的版本。本书使用Python 3完成。

一旦你充分地理解或学习使用了其中的一个，你可以很容易学到两个版本之间的区别，然后很容易的适应。困难的是学习编程和理解Python语言的核心，这是本书的目标。一旦你达到这个目标，你可以根据自己的情形很容易的使用Python 2或Python 3。

关于Python 2和Python 3的详细区别，请参考：
- [Python 2的未来](http://lwn.net/Articles/547191/)
- [将Python 2代码移植到Python 3](https://docs.python.org/3/howto/pyporting.html)
- [怎样书写能够同时运行在Python2 and 3中的代码](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef)
- [使用Python 3: 深度指南](http://python3porting.com)


## 程序员说了些什么

或许你会对顶尖的黑客，比如ESR，怎么看待Python感兴趣：

> Eric S. Raymond，是《The Cathedral and the Bazaar》的作者，也是发明开放源代码这一术语的人。他说，[Python已经成为他最喜欢的编程语言](http://www.python.org/about/success/esr/)。这篇文章给我第一次关注Python的真正灵感。

> Bruce Eckel，是著名的《Thinking in Java》和《Thinking in C++》的作者。他说，没有什么语言能比Python更能令他高效。他说，Python或许是唯一让程序员工作更简单的一个语言。请看完整的[采访](http://www.artima.com/intv/aboutme.html)。

> Peter Norvig，是著名的Lisp的作者，Google搜索质量主管（感谢Guido van Rossum指出）。他说[用Python编程就像是在写诗一样](https://news.ycombinator.com/item?id=1803815)。他还说，Python一直是Google的主要部分。你可以通过查看[Google Jobs](http://www.google.com/jobs/index.html)验证这句话。这个页面上显示出，Python知识是招聘软件工程师的要求之一。

--------------------------------------------------

### 继续阅读[安装](install.md)
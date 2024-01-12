# 关于Python

编程语言中有很少能像Python这样，即 _简单易学_ 又 _功能强大_。在学习的过程中，我们会惊喜地发现，我们可以很轻松的专注于问题的解决方案，而不是你正在使用的编程语言的语法以及结构。

Python的官方介绍：

> Python是一个简单易学、功能强大的编程语言。它的数据结构非常高效，对面向对象编程的实现也足够简单。Python优美的语法和动态类型，连同解释型特性一起，使其在多个平台的许多领域都成为脚本处理以及快速应用开发的理想语言。

在下一章，我将更详细地讨论这些特性。

## 名字背后的故事

Python语言的发明人Guido van Rossum以BBC的电视剧《Monty Python's Flying Circus》给这个语言命名。他不是特别喜欢那些为了食物而杀死动物的蛇，这些蛇会用它们长长的身体缠绕住那些动物从而勒死它们。

## Python的特点

### 简单

Python语言非常简约。阅读优秀的Python程序感觉就像阅读英语，而且是语法非常严格的英语。Python的这种伪代码特性是其最大强项之一，它可让你专注于解决问题的办法而不是语言本身。

### 容易学习

正如你即将看到的，Python非常容易上手。就像刚刚提到的，Python具有格外简单的语法。

### 免费开源

Python是一个 _FLOSS_（自由与开源软件）的例子。在一些简单的条款之下，你可以自由地分发这个软件的拷贝，阅读其源代码，修改它，或者将其一部分用到新的开源软件中。FLOSS基于共享知识社区的概念。这是Python的优势之一：它由Python社区创建并不断改进，这个社区希望Python变得越来越好。


### 高级语言

当你使用Python编写程序时，你永远不需要关心底层的细节，比如你的程序如何管理内存的使用等。

### 可移植

基于其开放源代码的特性，Python已经被移植到许多操作系统平台。只要在编程时避免使用与特定操作系统绑定的特性，你的Python程序可以不加修改地运行在这其中的任意平台。

你可以在GNU/Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acorn RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE，甚至PocketPC平台上使用Python。

你甚至可以使用[Kivy](http://kivy.org)平台为iOS（iPhone、iPad）和Android创建游戏。

### 解释型

这个特性解释起来稍微复杂一点。

使用编译型语言（像C或者C++）编写的程序，会由编译器根据一系列的配置和选项，将源代码（如C或者C++）转换成一种电脑能够识别的语言（二进制代码，也就是0和1）。在运行程序时，由加载程序将编译后的二进制代码从硬盘复制到内存，然后开始运行。

而Python不需要编译成二进制代码。你只需从源代码直接运行程序。在运行的时候，Python将源代码转换成一种称为字节码的中间格式，再将其翻译计算机可以识别的二进制代码，然后开始运行。事实上，这一切都让Python的使用更为简单，因为你不必担心程序的编译、链接加载等问题。这也使得你的Python程序更易于移植，因为你只需要复制你的Python程序到另外一台计算机，它就可以工作了！

### 面向对象

Python supports procedure-oriented programming as well as object-oriented programming (OOP). In _procedure-oriented_ languages, the program is built around procedures or functions which are nothing but reusable pieces of programs. In _object-oriented_ languages, the program is built around objects which combine data and functionality. Python has a very powerful but simplistic way of doing OOP, especially when compared to big languages like C++ or Java.
Python同时支持面向过程和面向对象编程。在 _面向过程_ 编程的时候，程序围绕着过程或函数（可重复使用的程序片段）构建。在 _面向对象_ 编程的时候，程序围绕着对象（数据和功能的组合）构建。相比于C++或者Java这种大型语言来说，Python具有强大且简洁的面向对象编程的方式。

### 可扩展

如果有一段代码很关键，需要能够快速运行，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。

### 可嵌入

你可以将Python嵌入到C/C++程序，让你的程序的用户获得 _脚本化_ 的能力。

### 庞大的扩展库

Python标准库非常庞大。它能够帮助你完成许多工作，包括正则表达式、生成文档、单元测试、线程、数据库、网页浏览器、CGI（公共网关接口）、FTP（文件传输协议）、电子邮件、XML（可扩展标记语言）、XML-RPC（远程方法调用）、HTML（超文本标记语言）、WAV（音频格式）文件、加密、GUI（图形用户界面）以及其它与特定操作系统相关的代码。这里需要强调一下，只要安装了Python，上面这些功能都可以做到。这被称作Python的 _开箱即用_ 哲学。

除了标准库，还有各式各样的其它高质量的扩展库，可以在[Python包索引](http://pypi.python.org/pypi)中找到它们。

### 小结

Python的确是一个令人激动的、功能强大的语言。Python将性能和特性结合得恰到好处，让我们使用Python编程既有趣又简单。

## Python 3 vs 2

如果你不关心Python 2和Python 3的区别，可以跳过这一节。但是必须知道你正在使用的Python版本。本书使用Python 3完成。

一旦你充分地理解或学习使用了两个版本中的一个，你会很容易了解两个版本之间的区别，也就可以轻而易举地切换到另外一个版本进行编程。重点是学习编程和理解Python语言的核心，这也是本书的目标。一旦你达成这个目标，你可以很容易的根据情况选择使用Python 2或Python 3。

关于Python 2和Python 3的详细区别，请参考：
- [Python 2的未来](http://lwn.net/Articles/547191/)
- [将Python 2代码移植到Python 3](https://docs.python.org/3/howto/pyporting.html)
- [怎样书写能够同时运行在Python2 and 3中的代码](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef)
- [使用Python 3: 深度指南](http://python3porting.com)

## 看看其他程序员怎么说的

You may find it interesting to read what great hackers like Eric S. Raymond (ESR) have to say about Python:

- _Eric S. Raymond_ is the author of "The Cathedral and the Bazaar" and is also the person who coined the term _Open Source_. He says that [Python has become his favorite programming language](http://www.python.org/about/success/esr/). This article was the real inspiration for my first brush with Python.
- _Bruce Eckel_ is the author of the famous 'Thinking in Java' and 'Thinking in C++' books. He says that no language has made him more productive than Python. He says that Python is perhaps the only language that focuses on making things easier for the programmer. Read the [complete interview](http://www.artima.com/intv/aboutme.html) for more details.
- _Peter Norvig_ is a well-known Lisp author and Director of Search Quality at Google (thanks to Guido van Rossum for pointing that out). He says that [writing Python is like writing in pseudocode](https://news.ycombinator.com/item?id=1803815). He says that Python has always been an integral part of Google. You can actually verify this statement by looking at the [Google Jobs](http://www.google.com/jobs/index.html) page which lists Python knowledge as a requirement for software engineers.

或许你感兴趣顶尖的黑客，比如Eric S. Raymond (ESR)，关于Python是怎么说的：

> _Eric S. Raymond_，是《The Cathedral and the Bazaar》的作者，也是发明 _开放源代码_ 这一术语的人。他说，[Python已经成为他最喜欢的编程语言](http://www.python.org/about/success/esr/)。这篇文章给了我关注Python的第一个灵感。

> _Bruce Eckel_，是著名的《Thinking in Java》和《Thinking in C++》的作者。他说，没有什么语言能比Python更能令他高效。他说Python或许是唯一让程序员工作更简单的编程语言。完整的采访请参考[这里](http://www.artima.com/intv/aboutme.html)。

> _Peter Norvig_，是另一个著名编程语言Lisp的作者，Google搜索质量主管（感谢Guido van Rossum指出）。他说[用Python编程就像是在写诗一样](https://news.ycombinator.com/item?id=1803815)。他还说，Python一直是Google代码的重要组成部分。你可以通过查看[Google Jobs](http://www.google.com/jobs/index.html)验证这句话。从这个页面可以看出，Python知识是Google招聘软件工程师的必备技能。

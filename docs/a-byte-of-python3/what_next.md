# 继续学习

如果你有认真通读本书之前的内容并且实践其中包含的大量例程，那么你现在一定可以熟练使用python了。
同时你可能也编写了一些程序用于验证python特性并提高你的python技能。如果还没有这样做的话，你应该去试试。
现在的问题是接下来应该做什么？

我建议你先解决下面的问题：

> 创建你自己的命令行版本的*通讯录程序*，利用它你可以浏览修改删除或搜索诸如朋友，家人，同事等联系人和他们的email地址/或电话号码等信息。这些信息必须存起来以便需要时提取。

思考下我们已经学到的各种知识，这个问题其实相当简单。
如果你感觉还是不好下手的话，这有一些提示。

创建一个表示联系人(persion)信息的类。使用字典存储联系人对象并以人物的名字作为字典键。
然后利用pickle模块把这些对象永久存储到你的硬盘中。最后通过字典的内建方法add, delete和modify分别增加删除修改联系人。

只要你有能力完成这个程序，你就可以自信的说你是一个python程序员了。那么现在马上给我[发送e-mail](http://www.swaroopch.com/contact/)好感谢我编写了如此强大的教程吧;-)当然这步是可选的但我还是希望你发过来。同时，也请考虑下[购买纸质书籍](http://www.swaroopch.com/buybook/)以支持本书的持续发展。

如果你觉得上面的程序太简单，这还有另一个：

> 实现[replace命令](http://unixhelp.ed.ac.uk/CGI/man-cgi?replace)。此命令用于在给定的文件列表中的所有文件中替换指定的字符串。

replace命令可以简单的执行字符串替换也可以复杂的进行模式查找(正则表达式)，这取决于你的意愿。

## 继续完成新的项目

如果你发现上述程序依然很简单，那么你可以看一下这个更加复杂的项目清单，用你自己的方法完成这些程序： https://github.com/thekarangoel/Projects#numbers (同样的清单还可以参考 [Martyr2's Mega Project List](http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/)).

更多的项目：

- [Exercises for Programmers: 57 Challenges to Develop Your Coding Skills](https://pragprog.com/book/bhwb/exercises-for-programmers)
- [Intermediate Python Projects](https://openhatch.org/wiki/Intermediate_Python_Workshop/Projects).

## 实例代码

学习程序设计最好的办法就是编写阅读大量代码：

- [Python Cookbook](http://code.activestate.com/recipes/langs/python/) 对于某些种类的问题Python Cookbook提供了许多解决问题的珍贵技巧和诀窍。此网是每个python用户都必读的。
- [Python Module of the Week](http://pymotw.com/2/contents.html) 是另外一个必读的网站，主要是[Python标准库](./stdlib.md#stdlib)的指南。

## 忠告

- [The Hitchhiker's Guide to Python!](http://docs.python-guide.org/en/latest/)
- [The Elements of Python Style](https://github.com/amontalenti/elements-of-python-style)
- [Python Big Picture](http://slott-softwarearchitect.blogspot.ca/2013/06/python-big-picture-whats-roadmap.html)
- ["Writing Idiomatic Python" ebook](http://www.jeffknupp.com/writing-idiomatic-python-ebook/) (paid)

## 视频

- [Full Stack Web Development with Flask](https://github.com/realpython/discover-flask)
- [PyVideo](http://www.pyvideo.org)

## 问题与解答

- [Official Python Dos and Don'ts](http://docs.python.org/3/howto/doanddont.html)
- [Official Python FAQ](http://www.python.org/doc/faq/general/)
- [Norvig's list of Infrequently Asked Questions](http://norvig.com/python-iaq.html)
- [Python Interview Q & A](http://dev.fyicenter.com/Interview-Questions/Python/index.html)
- [StackOverflow questions tagged with python](http://stackoverflow.com/questions/tagged/python)

## 教程

- [Hidden features of Python](http://stackoverflow.com/q/101268/4869)
- [What's the one code snippet/python trick/etc did you wish you knew when you learned python?](http://www.reddit.com/r/Python/comments/19dir2/whats_the_one_code_snippetpython_tricketc_did_you/)
- [Awaretek's comprehensive list of Python tutorials](http://www.awaretek.com/tutorials.html)

## 讨论组

如果你被某个问题难住了，也不知道找谁求助，那么[python-tutor list](http://mail.python.org/mailman/listinfo/tutor)是个提问的好地方。

提问之前需要先做做功课，你应该自己先尝试解决问题，然后[智慧的提问](http://catb.org/~esr/faqs/smart-questions.html)

## 新闻

如果你想了解python的最新动态，请关注[Official Python Planet](http://planet.python.org)。

## 安装库

Python包索引[Python Package Index](http://pypi.python.org/pypi)拥有数量巨大的开源库，你可以在自己的程序中使用它们。

安装和使用这些库，你可以使用[pip](http://www.pip-installer.org/en/latest/)工具。

## 创建一个网站

你可以使用[Django](https://www.djangoproject.com/)创建你自己的网站，本文后面会教你一步一步学习使用Django Web框架)。（我自己的喜好，原文写的是Flask框架，但是这个框架动不动就好几个月都不更新，我想还是选择一个由团队持续维护的框架比较靠谱）

## 编写GUI应用程序

如果你想使用Python创建自己的GUI应用程序。那么可以使用已绑定到Python上的GUI(图形用户界面)库。
绑定允许你在自己的程序中使用这些库，而库本身是用C/C++或其它语言编写的。

使用Python你可以选择很多种GUI库：

- Kivy
    - http://kivy.org

- PyGTK
    - GTK+工具包的python绑定。它是GNOME的基础。GTK+含有很多奇怪的用法，不过一旦熟悉它你就能够快速创建GUI应用了。其中Glade图形界面设计器是必不可少的。GTK+的文档仍然完善中。GTK+在linux上工作的很好，但其windows实现仍未完成。 另外使用GTK+你既可以创建开源也可以创建私有软件。 入门可以阅读[PyGTK教程](http://www.pygtk.org/tutorial.html).

- PyQt

    - 这是绑定到Python的Qt工具包，它是创建KDE的基石。 Qt非常易用，功能又很强大，尤其是仰仗于它的Qt Designer与出色的Qt文档。 如果你在创建开源软件(GPL’ed)则PyQt是免费的, 相反创建商业的私有软件的用户就要掏银子买它了。 从Qt4.5开始你同样可以用它创建非GPL软件。 作为入门可以阅读[PyQt5从入门到精通](https://www.gitbook.com/book/borisliu/pyqt5-gui-dev/details)。

- wxPython

    - 这是绑定到python的wxWidgets工具包。 wxPython有一定的学习曲线。但是具有很强的可移植性，可以运行在linux，windows，Mac甚至是嵌入式平台之上。 wxPython拥有很多可用的IDE，其中包括GUI设计器和诸如SPE(Stani的python编辑器)(http://spe.pycs.net)和wxGlade(http://wxglade.sourceforge.net/)的开发工具。 使用wxPython你既可以创建开源软件也可以创建私有软件。入门可以阅读wxPython教程(http://zetcode.com/wxpython/)

### GUI小结

更多的选择参见[GuiProgramming wiki page at the official python website](http://www.python.org/cgi-bin/moinmoin/GuiProgramming)。

很不幸，python没有一个标准GUI工具。我建议根据你的情况选择上面的工具。考虑的第一歌因素是你是否愿意付费使用GUI工具。第二你是否希望程序只运行在windows或mac或linux还是希望都能运行。第三对于linux平台，你是一个KDE还是一个GNOME用户呢。

【译者】：对于国内用户来说，首选PyQt5平台，首先Qt工具是这几个工具中使用最广泛的，有一些知名的公司如LG、松下、ABB等都采用Qt作为GUI开发平台；其次，PyQt是这几个工具中升级更新最频繁的，选用一个长期不更新的软件包会各种奇葩的坑等着你去经历；最后，Qt和PyQt的中文的开发文档以及社区也是最完整的。还有，GPL版权（此处省去23412字）。

更详细广泛的分析，见Python Papers 第26页卷3问题1(http://archive.pythonpapers.org/ThePythonPapersVolume3Issue1.pdf)

## 各种python实现

一个程序设计语言通常包含两部分 – 语言和软件。语言指出如何编写程序。而软件用来运行我们的程序。

我们一直在用CPython运行我们的程序，之所以称为CPython是因为它是用C语言实现的并且为标准Python解释器。

另外还有其它的软件也可以运行python程序：

- [Jython](http://www.jython.org)
    - 一个运行在Java平台的Python实现。这意味着你可以在Python语言内部使用Java库和类，反之亦然。

- [IronPython](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython)
    - 一个运行在.NET平台的Python实现。即你可以在Python语言内部使用.NET库和类，反之亦然。

- [PyPy](http://codespeak.net/pypy/dist/pypy/doc/home.html)
    - 一个用python写的python实现！这是一个研究项目，用于使之可以快而容易的改进解释器，因为解释器本身就是用动态语言编写的。（而不是类似上面的C, java或C#等静态语言）

除此之外还有CLPython(http://common-lisp.net/project/clpython/)一个Common Lisp编写的python实现。[Brython](http://brython.info/)是一个运行在JavaScript解释器之上的IronPython的接口，这可能意味着你可以使用python(替代JavaScript)编写web浏览器程序(“Ajax”)。

以上的每个实现都有自己的擅长领域。

## 函数式编程 (为更高级别用户) {#functional-programming}

当你要开始完成较大规模的应用程序的时候，你一定要学习一下函数式编程范式，这是与我们前面所学的[面向对象编程](./oop.md)相对应的另外一种编程范式：

- [Functional Programming Howto by A.M. Kuchling](http://docs.python.org/3/howto/functional.html)
- [Functional programming chapter in 'Dive Into Python' book](http://www.diveintopython.net/functional_programming/index.html)
- [Functional Programming with Python presentation](http://ua.pycon.org/static/talks/kachayev/index.html)
- [Funcy library](https://github.com/Suor/funcy)
- [PyToolz library](http://toolz.readthedocs.org/en/latest/)

## Summary

现在我们已经来到本书的结尾了。不过据说，结束意味着另一个开始！你现在是一个满腔热情的Python程序员，很可能摩拳擦掌准备利用Python解决大量问题。现在你可以让计算机自动完成许多以前无法想象的事情或是编写游戏或是更多更多。既然如此！那就行动起来大干一场吧！

--------------------------------------------------

### 继续阅读[附录：免费/自由和开放源码软件](floss.md)
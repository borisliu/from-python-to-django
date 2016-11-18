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

If you want to learn what is the latest in the world of Python, then follow the [Official Python Planet](http://planet.python.org).

## Installing libraries

There are a huge number of open source libraries at the [Python Package Index](http://pypi.python.org/pypi) which you can use in your own programs.

To install and use these libraries, you can use [pip](http://www.pip-installer.org/en/latest/).

## Creating a Website

Learn [Flask](http://flask.pocoo.org) to create your own website. Some resources to get started:

- [Flask Official Quickstart](http://flask.pocoo.org/docs/quickstart/)
- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Example Flask Projects](https://github.com/mitsuhiko/flask/tree/master/examples)

## Graphical Software

Suppose you want to create your own graphical programs using Python. This can be done using a GUI (Graphical User Interface) library with their Python bindings. Bindings are what allow you to write programs in Python and use the libraries which are themselves written in C or C++ or other languages.

There are lots of choices for GUI using Python:

- Kivy
    - http://kivy.org

- PyGTK
    - This is the Python binding for the GTK+ toolkit which is the foundation upon which GNOME is built. GTK+ has many quirks in usage but once you become comfortable, you can create GUI apps fast. The Glade graphical interface designer is indispensable. The documentation is yet to improve. GTK+ works well on GNU/Linux but its port to Windows is incomplete. You can create both free as well as proprietary software using GTK+. To get started, read the [PyGTK tutorial](http://www.pygtk.org/tutorial.html).

- PyQt
    - This is the Python binding for the Qt toolkit which is the foundation upon which the KDE is built. Qt is extremely easy to use and very powerful especially due to the Qt Designer and the amazing Qt documentation. PyQt is free if you want to create open source (GPL'ed) software and you need to buy it if you want to create proprietary closed source software. Starting with Qt 4.5 you can use it to create non-GPL software as well. To get started, read about [PySide](http://qt-project.org/wiki/PySide).

- wxPython
    - This is the Python bindings for the wxWidgets toolkit. wxPython has a learning curve associated with it. However, it is very portable and runs on GNU/Linux, Windows, Mac and even embedded platforms. There are many IDEs available for wxPython which include GUI designers as well such as [SPE (Stani's Python Editor)](http://spe.pycs.net/) and the [wxGlade](http://wxglade.sourceforge.net/) GUI builder. You can create free as well as proprietary software using wxPython. To get started, read the [wxPython tutorial](http://zetcode.com/wxpython/). 

### Summary of GUI Tools

For more choices, see the [GuiProgramming wiki page at the official python website](http://www.python.org/cgi-bin/moinmoin/GuiProgramming).

Unfortunately, there is no one standard GUI tool for Python. I suggest that you choose one of the above tools depending on your situation. The first factor is whether you are willing to pay to use any of the GUI tools. The second factor is whether you want the program to run only on Windows or on Mac and GNU/Linux or all of them. The third factor, if GNU/Linux is a chosen platform, is whether you are a KDE or GNOME user on GNU/Linux.

For a more detailed and comprehensive analysis, see Page 26 of the ['The Python Papers, Volume 3, Issue 1' (PDF)](http://archive.pythonpapers.org/ThePythonPapersVolume3Issue1.pdf).

## Various Implementations

There are usually two parts a programming language - the language and the software. A language is _how_ you write something. The software is _what_ actually runs our programs.

We have been using the _CPython_ software to run our programs. It is referred to as CPython because it is written in the C language and is the _Classical Python interpreter_.

There are also other software that can run your Python programs:

- [Jython](http://www.jython.org)
    - A Python implementation that runs on the Java platform. This means you can use Java libraries and classes from within Python language and vice-versa.

- [IronPython](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython)
    - A Python implementation that runs on the .NET platform. This means you can use .NET libraries and classes from within Python language and vice-versa.

- [PyPy](http://codespeak.net/pypy/dist/pypy/doc/home.html)
    - A Python implementation written in Python! This is a research project to make it fast and easy to improve the interpreter since the interpreter itself is written in a dynamic language (as opposed to static languages such as C, Java or C# in the above three implementations)

There are also others such as [CLPython](http://common-lisp.net/project/clpython/) - a Python implementation written in Common Lisp and [Brython](http://brython.info/) which is an implementation on top of a JavaScript interpreter which could mean that you can use Python (instead of JavaScript) to write your web-browser ("Ajax") programs.

Each of these implementations have their specialized areas where they are useful.

## Functional Programming (for advanced readers) {#functional-programming}

When you start writing larger programs, you should definitely learn more about a functional approach to programming as opposed to the class-based approach to programming that we learned in the [object-oriented programming chapter](./oop.md#oop):

- [Functional Programming Howto by A.M. Kuchling](http://docs.python.org/3/howto/functional.html)
- [Functional programming chapter in 'Dive Into Python' book](http://www.diveintopython.net/functional_programming/index.html)
- [Functional Programming with Python presentation](http://ua.pycon.org/static/talks/kachayev/index.html)
- [Funcy library](https://github.com/Suor/funcy)
- [PyToolz library](http://toolz.readthedocs.org/en/latest/)

## Summary

We have now come to the end of this book but, as they say, this is the _the beginning of the end_!. You are now an avid Python user and you are no doubt ready to solve many problems using Python. You can start automating your computer to do all kinds of previously unimaginable things or write your own games and much much more. So, get started!

---

[^1]: Create a class to represent the person's information. Use a dictionary to store person objects with their name as the key. Use the pickle module to store the objects persistently on your hard disk. Use the dictionary built-in methods to add, delete and modify the persons.
# What Next

If you have read this book thoroughly till now and practiced writing a lot of programs, then you must have become comfortable and familiar with Python. You have probably created some Python programs to try out stuff and to exercise your Python skills as well. If you have not done it already, you should. The question now is 'What Next?'.

I would suggest that you tackle this problem:

> Create your own command-line *address-book* program using which you can browse, add, modify, delete or search for your contacts such as friends, family and colleagues and their information such as email address and/or phone number. Details must be stored for later retrieval.

This is fairly easy if you think about it in terms of all the various stuff that we have come across till now. If you still want directions on how to proceed, then here's a hint [^1].

Once you are able to do this, you can claim to be a Python programmer. Now, immediately [send me an email]({{ book.contactUrl }}) thanking me for this great book ;-). This step is optional but recommended. Also, please consider [buying a printed copy]({{ book.buyBookUrl }}) to support the continued development of this book.

If you found that program easy, here's another one:

> Implement the [replace command](http://unixhelp.ed.ac.uk/CGI/man-cgi?replace). This command will replace one string with another in the list of files provided.

The replace command can be as simple or as sophisticated as you wish, from simple string substitution to looking for patterns (regular expressions).

## Next Projects

If you found above programs easy to create, then look at this comprehensive list of projects and try writing your own programs: https://github.com/thekarangoel/Projects#numbers (the same list is also at [Martyr2's Mega Project List](http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/)).

Also see:

- [Exercises for Programmers: 57 Challenges to Develop Your Coding Skills](https://pragprog.com/book/bhwb/exercises-for-programmers)
- [Intermediate Python Projects](https://openhatch.org/wiki/Intermediate_Python_Workshop/Projects).

## Example Code

The best way to learn a programming language is to write a lot of code and read a lot of code:

- [Python Cookbook](http://code.activestate.com/recipes/langs/python/) is an extremely valuable collection of recipes or tips on how to solve certain kinds of problems using Python. This is a must-read for every Python user.
- [Python Module of the Week](http://pymotw.com/2/contents.html) is another excellent must-read guide to the [Standard Library](./stdlib.md#stdlib).

## Advice

- [The Hitchhiker's Guide to Python!](http://docs.python-guide.org/en/latest/)
- [The Elements of Python Style](https://github.com/amontalenti/elements-of-python-style)
- [Python Big Picture](http://slott-softwarearchitect.blogspot.ca/2013/06/python-big-picture-whats-roadmap.html)
- ["Writing Idiomatic Python" ebook](http://www.jeffknupp.com/writing-idiomatic-python-ebook/) (paid)

## Videos

- [Full Stack Web Development with Flask](https://github.com/realpython/discover-flask)
- [PyVideo](http://www.pyvideo.org)

## Questions and Answers

- [Official Python Dos and Don'ts](http://docs.python.org/3/howto/doanddont.html)
- [Official Python FAQ](http://www.python.org/doc/faq/general/)
- [Norvig's list of Infrequently Asked Questions](http://norvig.com/python-iaq.html)
- [Python Interview Q & A](http://dev.fyicenter.com/Interview-Questions/Python/index.html)
- [StackOverflow questions tagged with python](http://stackoverflow.com/questions/tagged/python)

## Tutorials

- [Hidden features of Python](http://stackoverflow.com/q/101268/4869)
- [What's the one code snippet/python trick/etc did you wish you knew when you learned python?](http://www.reddit.com/r/Python/comments/19dir2/whats_the_one_code_snippetpython_tricketc_did_you/)
- [Awaretek's comprehensive list of Python tutorials](http://www.awaretek.com/tutorials.html)

## Discussion

If you are stuck with a Python problem, and don't know whom to ask, then the [python-tutor list](http://mail.python.org/mailman/listinfo/tutor) is the best place to ask your question.

Make sure you do your homework by trying to solving the problem yourself first and [ask smart questions](http://catb.org/~esr/faqs/smart-questions.html).

## News

If you want to learn what is the latest in the world of Python, then follow the [Official Python Planet](http://planet.python.org).

## Installing libraries

There are a huge number of open source libraries at the [Python Package Index](http://pypi.python.org/pypi) which you can use in your own programs.

To install and use these libraries, you can use [pip](http://www.pip-installer.org/en/latest/).

## Creating a Website

Learn [Flask](http://flask.pocoo.org) to create your own website. Some resources to get started:

- [Flask Official Quickstart](http://flask.pocoo.org/docs/quickstart/)
- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Example Flask Projects](https://github.com/mitsuhiko/flask/tree/master/examples)

## Graphical Software

Suppose you want to create your own graphical programs using Python. This can be done using a GUI (Graphical User Interface) library with their Python bindings. Bindings are what allow you to write programs in Python and use the libraries which are themselves written in C or C++ or other languages.

There are lots of choices for GUI using Python:

- Kivy
    - http://kivy.org

- PyGTK
    - This is the Python binding for the GTK+ toolkit which is the foundation upon which GNOME is built. GTK+ has many quirks in usage but once you become comfortable, you can create GUI apps fast. The Glade graphical interface designer is indispensable. The documentation is yet to improve. GTK+ works well on GNU/Linux but its port to Windows is incomplete. You can create both free as well as proprietary software using GTK+. To get started, read the [PyGTK tutorial](http://www.pygtk.org/tutorial.html).

- PyQt
    - This is the Python binding for the Qt toolkit which is the foundation upon which the KDE is built. Qt is extremely easy to use and very powerful especially due to the Qt Designer and the amazing Qt documentation. PyQt is free if you want to create open source (GPL'ed) software and you need to buy it if you want to create proprietary closed source software. Starting with Qt 4.5 you can use it to create non-GPL software as well. To get started, read about [PySide](http://qt-project.org/wiki/PySide).

- wxPython
    - This is the Python bindings for the wxWidgets toolkit. wxPython has a learning curve associated with it. However, it is very portable and runs on GNU/Linux, Windows, Mac and even embedded platforms. There are many IDEs available for wxPython which include GUI designers as well such as [SPE (Stani's Python Editor)](http://spe.pycs.net/) and the [wxGlade](http://wxglade.sourceforge.net/) GUI builder. You can create free as well as proprietary software using wxPython. To get started, read the [wxPython tutorial](http://zetcode.com/wxpython/). 

### Summary of GUI Tools

For more choices, see the [GuiProgramming wiki page at the official python website](http://www.python.org/cgi-bin/moinmoin/GuiProgramming).

Unfortunately, there is no one standard GUI tool for Python. I suggest that you choose one of the above tools depending on your situation. The first factor is whether you are willing to pay to use any of the GUI tools. The second factor is whether you want the program to run only on Windows or on Mac and GNU/Linux or all of them. The third factor, if GNU/Linux is a chosen platform, is whether you are a KDE or GNOME user on GNU/Linux.

For a more detailed and comprehensive analysis, see Page 26 of the ['The Python Papers, Volume 3, Issue 1' (PDF)](http://archive.pythonpapers.org/ThePythonPapersVolume3Issue1.pdf).

## Various Implementations

There are usually two parts a programming language - the language and the software. A language is _how_ you write something. The software is _what_ actually runs our programs.

We have been using the _CPython_ software to run our programs. It is referred to as CPython because it is written in the C language and is the _Classical Python interpreter_.

There are also other software that can run your Python programs:

- [Jython](http://www.jython.org)
    - A Python implementation that runs on the Java platform. This means you can use Java libraries and classes from within Python language and vice-versa.

- [IronPython](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython)
    - A Python implementation that runs on the .NET platform. This means you can use .NET libraries and classes from within Python language and vice-versa.

- [PyPy](http://codespeak.net/pypy/dist/pypy/doc/home.html)
    - A Python implementation written in Python! This is a research project to make it fast and easy to improve the interpreter since the interpreter itself is written in a dynamic language (as opposed to static languages such as C, Java or C# in the above three implementations)

There are also others such as [CLPython](http://common-lisp.net/project/clpython/) - a Python implementation written in Common Lisp and [Brython](http://brython.info/) which is an implementation on top of a JavaScript interpreter which could mean that you can use Python (instead of JavaScript) to write your web-browser ("Ajax") programs.

Each of these implementations have their specialized areas where they are useful.

## Functional Programming (for advanced readers) {#functional-programming}

When you start writing larger programs, you should definitely learn more about a functional approach to programming as opposed to the class-based approach to programming that we learned in the [object-oriented programming chapter](./oop.md#oop):

- [Functional Programming Howto by A.M. Kuchling](http://docs.python.org/3/howto/functional.html)
- [Functional programming chapter in 'Dive Into Python' book](http://www.diveintopython.net/functional_programming/index.html)
- [Functional Programming with Python presentation](http://ua.pycon.org/static/talks/kachayev/index.html)
- [Funcy library](https://github.com/Suor/funcy)
- [PyToolz library](http://toolz.readthedocs.org/en/latest/)

## Summary

We have now come to the end of this book but, as they say, this is the _the beginning of the end_!. You are now an avid Python user and you are no doubt ready to solve many problems using Python. You can start automating your computer to do all kinds of previously unimaginable things or write your own games and much much more. So, get started!

---

[^1]: Create a class to represent the person's information. Use a dictionary to store person objects with their name as the key. Use the pickle module to store the objects persistently on your hard disk. Use the dictionary built-in methods to add, delete and modify the persons.

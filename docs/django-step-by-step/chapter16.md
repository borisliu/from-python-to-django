# Django Step by Step (十六)

## 1 引言

[Django](https://www.djangoproject.com/) 中的模板系统可以被自由扩展，如自定义 filter, 自定义 Tag 等。其中 filter 用于对变量的处理。而 Tag 则功能强大，几乎可以做任何事情。我认为 Tag 的好处有非常多，比如：

  * 可以简单化代码的生成。一个 Tag 相当于一个代码片段，把重复的东西做成 Tag 可以避免许多重复的工作。 
  * 可以用来组合不同的应用。将一个应用的展示处理成 Tag 的方式，这样就可以在一个模板中组合不同的应用展示 Tag，而且修改模板也相对容易。 

如果要自定义 Tag ，那么要了解 Tag 的处理过程。在 Django 中， Tag 的处理分为两步。

  1. 编译。即把 Tag 编译为一系列的 `django.template.Node` 结点。 
  2. 渲染(Render)。即对每个 Node 调用它们的 `render()` 方法，然后将输出结果拼接起来。 

因此自定义一个 Tag ，你需要针对这两步处理来做工作。

在 [The Django template language: For Python programmers](https://docs.djangoproject.com/en/2.0/ref/templates/api/) 文档中讲解了一些例子。大家可以看一下。

那么下面，我将实现一个显示日历的自定义 Tag 。

## 2 下载 HTMLCalendar 模块并安装

不想全部自已做，因此找了一个现成的模块。去 HTMLCalender 的主页下载这个模块。

然后解压到一个目录下，执行安装:

python setup.py install

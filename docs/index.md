从Python到Django CMS入门教程
===================

## 前言

Python可能是为数不多的既简单又强大的几个编程语言之一。它对初学者和专家都很适合，更重要的是，用Python编程很有趣。本书目的是帮助你学习这个奇妙的语言，展示如何快速而方便地完成任务——事实上的“对编程问题的完美抗毒剂”。

使用Python构建的Web开发框架Django是开发Web应用程序的利器，而Django-CMS更是提供了页面在线编辑等现代CMS才具有的功能。这一系列软件应对目前的Web应用开发是足够了。


基于上述这些问题，本人决定向limodou，Zoom.Quiet等大牛学习，重新翻译并整理一下这些文档，给那些零起点的程序员一个完整的入门文档，学习路径是这样的：

```
  	Python3--->Django1.6--->Django-CMS3
```

## 开发环境

本文的范例基于SublimeText3编辑器完成的。因此，你需要准备以下这些软件：

* [SublimeText3](http://www.sublimetext.com/3)编辑器，不用费劲找破解版了，不注册的话顶多弹出注册的提示框，叉掉就没有问题，不存在试用期结束之后无法使用的问题。

* [Python3的安装文件](http://www.python.org/getit/)，根据你自己的操作系统安装，"下一步&下一步"就能搞定，无需多说。

* 用virtualenv搭建Django和Django-CMS的开发环境，后文会详细描述。

## 开始学习

根据自己的情况选择从哪里开始学习，如果你已经有了一定的基础，你可以选择跳过某些章节，对于大多数初学者来讲，学习的路径如下：

### 1. [搭建Python开发环境](introduction/index)。
### 2. [简明Python教程](a-byte-of-python3/index)。
### 3. [Django step by step](django-step-by-step/index)。
### 4. [Django-CMS官方文档中文翻译](django-cms/index)。

本文托管在[GitHub](https://github.com/borisliu/from-python-to-django)，如果有问题请在线[提交](https://github.com/borisliu/from-python-to-django/issues)。

## 附：参考资料

Python和Django很有趣，但是我一直以来都在纠结，是否要将自己学习Django的过程写下来。之所以会有这个问题，主要还是最近在对Django的学习过程中遇到了一些问题，归纳起来主要有以下几个：

* 以前学习的是Python 2.x的语法，基于与时俱进的原则，这个时候重新拾起来应该从Python 3开始了，但是很多老的文档仍然以Python 2为主。

* Python入门的文档中，《a byte of python》是最棒的，中文名叫[《简明Python教程》](http://zhgdg.gitcafe.com/static/doc/byte_of_python.html)，翻译过来很多错别字，看得我比较费劲。

* Django的入门文档中，最好的是[《Django step by step》](http://www.lhelper.org/dev/django_step_by_step/newtest/doc/)，但是文档太老了，还是照着Django 0.95版本写的，很多语法在最新的Django 1.6中都已经改变了，于是我只好一点一点查[Django官方文档](https://docs.djangoproject.com/en/1.6/)，E文的，看起来老费劲了。Django官方文档的[中文翻译](http://django-chinese-docs-16.readthedocs.org/en/latest/)还没有写完，很难能作为参考。

* 为了能够利用Python和Django快速搭建网站，我需要一个CMS系统，在Pythonic中，最活跃的就属[Django-CMS](http://www.django-cms.org/)，但是没有完整的中文文档。

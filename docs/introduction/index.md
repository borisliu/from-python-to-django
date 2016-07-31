# 搭建Python开发环境
==========

## 安装Python

Python的开发环境是比较简单的，到[http://python.org/getit/]()去下载对应的Python3安装包，本文使用的是Python 3.3.3，然后保留默认选项完成安装就是了。

我的开发环境不会修改操作系统的PATH路径，原因是我的电脑上安装了好几个版本的Python，使用的时候我会用绝对路径引用Python程序。一般情况下使用virtualenv会把PATH路径自动设置好。

调出你的终端（cmd），输入

```
    c:\python33\python
```

如果出现下面的提示，那么说明你已经安装成功了。

![](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/installpython.png)

Python环境搭好之后首先要做的就是这个：

```
    print('hello world!')
```

恭喜你！都会抢答了!

## 安装setuptools

setuptools绝对是个好东西，它可以自动的安装模块，只需要你提供给它一个模块名字就可以了，并且自动帮你解决模块的依赖问题。
你可以到[the Python Package Index](https://pypi.python.org/pypi)下载，如果你对E文看得不爽，可以直接点击[下载setuptools-2.0.2.tar.gz](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/setuptools-2.0.2.tar.gz)，之后解压缩，在命令行窗口进入到解压缩之后的目录中，运行以下命令：

```
    c:\python33\python setup.py install
```

完成安装。

## 安装pip

pip可以很方便的安装、卸载和管理Python的包。直接[下载pip-1.5.tar.gz](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/setuptools-2.0.2.tar.gz)，解压缩之后，在命令行窗口进入解压缩之后的目录中，运行以下命令：

```
    c:\python33\python setup.py install
```

完成安装。

## 安装virtualenv

virtualenv可以建立多个独立的虚拟环境，各个环境中拥有自己的python解释器和各自的package包，互不影响。
直接[下载virtualenv-1.11.tar.gz](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/virtualenv-1.11.tar.gz)，解压缩之后，在命令行窗口进入解压缩之后的目录中，运行以下命令：

```
    c:\python33\python setup.py install
```

完成安装。

pip和virtualenv可以很好的协同工作，同时使用这两个工具非常方便。用virtualenv env1就可以创建一个名为env1的虚拟环境了，进入这个虚拟环境后，再使用pip install安装其它的package就只会安装到这个虚拟环境里，不会影响其它虚拟环境或系统环境。接下来我们要用这个工具创建我们自己的开发环境。

## 安装Django1.6

首先创建一个virtualenv的目录，用来存放Python的虚拟环境，我是创建在D盘。

```
    d:
    mkdir virtualenv
    cd virtualenv
```

然后，创建我们的Django虚拟环境，用以下命令，注意，这里需要联网下载Django的安装包，首先确保你的电脑可以访问互联网。

```
    c:\python33\scripts\virtualenv django
    cd django
    scripts\activate.bat
```

这个时候你应该可以看到提示符前面增加了“(django)”的字样，如下所示：

![](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/virtualenv.png)

这个时候你的virtualenv就已经激活了，你再输入命令：

```
    python
```

的时候，就会使用这个虚拟环境下面的Python。请注意，下面的教程我么都是在这个环境下面运行的，每一次你开始学习的时候都要首先“激活”这个虚拟环境。

下面我们来安装Django。在虚拟环境下面，键入：

```
    pip install django
```

会自动联网下载并安装django。

## 安装Django-CMS

Django-CMS3尚处于beta状态，我们在虚拟环境中用以下命令安装beta版本：

```
    pip install https://github.com/divio/django-cms/archive/3.0.0.beta3.zip
```

pip会自动将依赖的包全部安装好。

## 完结！ 

--------------------------------------------------

### 继续阅读[简明Python教程](a-byte-of-python3/index)
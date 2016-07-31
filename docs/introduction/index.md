# 搭建Python开发环境
==========

## 安装Python

Python的开发环境是比较简单的，到[https://www.python.org/downloads/](https://www.python.org/downloads/)去下载对应的Python3安装包，安装的时候勾选上修改PATH的选项，然后完成安装就是了。本文使用的是Python 3.5.2。

调出你的终端（cmd），输入

```
    python
```

如果出现下面的提示，那么说明你已经安装成功了。

![](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/installpython.png)

Python环境搭好之后首先要做的就是这个：

```
    print('hello world!')
```

恭喜你！都会抢答了!

## 安装virtualenv

virtualenv可以建立多个独立的虚拟环境，各个环境中拥有自己的python解释器和各自的package包，互不影响。
使用Python自带的pip工具可以很方便的安装、卸载和管理Python的包。

```
    pip install virtualenv
```

完成安装。

pip和virtualenv可以很好的协同工作，同时使用这两个工具非常方便。
用virtualenv env1就可以创建一个名为env1的虚拟环境了，进入这个虚拟环境后，再使用pip install安装其它的package就只会安装到这个虚拟环境里，不会影响其它虚拟环境或系统环境。
接下来我们要用这个工具创建我们自己的开发环境。

## 安装Django1.9

首先创建一个virtualenv的目录，用来存放Python的虚拟环境，我是创建在D盘。

```
    d:
    mkdir virtualenv
    cd virtualenv
```

然后，创建我们的Django虚拟环境，用以下命令，注意，这里需要联网下载Django的安装包，首先确保你的电脑可以访问互联网。

```
    virtualenv django
    cd django
    scripts\activate.bat
```

这个时候你应该可以看到提示符前面增加了“(django)”的字样，如下所示：

![](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/introduction/virtualenv.png)

这个时候你的virtualenv就已经激活了，你再输入命令：

```
     (env) $ python
```

的时候，就会使用这个虚拟环境下面的Python。请注意，下面的教程我么都是在这个环境下面运行的，每一次你开始学习的时候都要首先“激活”这个虚拟环境。

下面我们来安装Django。在虚拟环境下面，键入：

```
    (env) $ pip install django
```

会自动联网下载并安装django，让我们检查一下django是否已经正确安装，输入下面的命令创建第一个django工程：

```
    (env) $ django-admin startproject helloworld
    (env) $ cd helloworld
    (env) $ python manage.py runserver
```
然后使用浏览器打开这个地址[http://127.0.0.1:8000/](http://127.0.0.1:8000/)就可以看到一个欢迎页面了。

## 安装Django-CMS

首先安装djangocms-installer，然后创建一个空的目录并键入：

```
    (env) $ pip install djangocms-installer
    (env) $ mkdir hellocms
    (env) $ cd hellocms
    (env) $ djangocms -p . hellocms
```

再次使用浏览器打开[http://127.0.0.1:8000/](http://127.0.0.1:8000/)，就会看到django-cms的首页面了。

## 完结！ 

--------------------------------------------------

### 继续阅读[简明Python教程](a-byte-of-python3/index.md)
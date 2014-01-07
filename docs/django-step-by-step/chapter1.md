# Django Step by Step (一)
=====================

## 1. 开篇

Django 是新近出来的 Rails 方式的 web 开发框架。Django 从我个人的感觉上来看，它的功能更强大，社区也很活跃，高手众多，发展也是极为迅速。我个人很看好。但是由于 Django 的教程过于想把它的特色展示给大家，因此，对于初学者来说一下子接触的东西太多，反倒让大家很难理解。于是我想从最最简单的例子做起，并且记录下来，并且将其形成一个教程。

## 2. Django的入门体验

下面我把我所尝试写最简单的 Hello, Django! 的例子写出来。

### 2.1 生成项目目录

Django 是一个框架，它有特殊的配置要求，因此一般不需要手工创建目录之类的工作， Django 提供了 django-admin.py 可以做这件事。

```
python \virtualenv\django\Scripts\django-admin.py startproject newtest
```

这样就在当前目录下创建了一个 newtest 目录，里面有一个文件和一个目录：

> 这个 newtest 将是我们以后工作的目录，许多讲解都是基于这个目录的。

> manage.py
> 提供简单化的 django-admin.py 命令，特别是可以自动进行 DJANGO_SETTINGS_MODULES 和 PYTHONPATH 的处理，而没有这个命令，处理上面环境变量是件麻烦的事情

> newtest工程下面的newtest目录是你项目的实际上的Python包目录。目录名就是Python包的名字，如果你需要引入该目录下面的文件，就需要使用这个名字（例如newtest.urls）

> newtest\__init__.py
> 表示这是一个 Python 的包

> newtest\settings.py
> 它是django的配置文件

> newtest\uls.py
> url映射处理文件，Django 的url映射是url对于某个模块方法的映射

> newtest\wsgi.py: 如果你的项目要加载到一个WSGI的Web服务器中，这是一个入口文件

虽然 django-admin.py 为我们生成了许多东西， 而且这些东西在以后的开发中你都需要熟悉，但现在我们的目标是最简单的体验，就认为我们不需要知道它们都有什么用吧。

项目创建好了，那么我们可以启动服务器吗？ Django 为了开发方便，自带了一个用于开发的 web server。

### 2.2 启动 web server

别急呀，还没看见 Hello, Django! 在哪里呢。是的，我只是想看一看， Django 能否启动。

```
python manage.py runserver
```

一旦出现:

```
Validating models...

0 errors found
January 07, 2014 - 14:59:55
Django version 1.6, using settings 'newtest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

说明 Django 真的启来了。在浏览器中看一下，有一个祝贺页面，说明成功了。

![祝贺页面](https://raw.github.com/borisliu/from-python-to-django-cms/master/docs/django-step-by-step/welcome.png)

### 2.3 增加一个helloworld的app吗？

在 Django 中绝大多数应用都是以app形式存在的，但一定要加吗？其实并不需要。在 Django 中，每个app就是一个子包，真正调用时需要通过 URL Dispatch 来实现url与模块方法的映射。这是 Django 的一大特色，但也是有些麻烦的地方。不用它，你无法发布一个功能，如果在 Django 中存在一种缺省的简单映射的方式，这样我想可以大大提高 Django 的入门体验度。

因此根据 URL Dispatch 的机制，我们只要保证 Django 可以在正确的地方找到方法进行调用即可。那么我们就根本不去创建一个app了。

在 newtest 目录下创建一个文件 helloworld.py 内容为:

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django.")
```

### 2.4 修改urls.py

没办法，不改不行啊，内容为:

```
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^newtest/', include('newtest.apps.foo.urls.foo')),
    (r'^$', 'newtest.helloworld.index'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
```

好了。保存了。上面的 r'^$' 是为了匹配空串，也就是形如: http://localhost:8000/ 。如果这时 web server 已经启动了，那么直接刷新页面就行了。

现在觉得 Django 是不是简单多了，除了创建一个项目的操作，然后可能要修改两个配置文件，其它还都简单吧。

## 3. 结论

Django 本身的确是一种松散的框架组合，它既复杂又简单。复杂是因为如果你想使用它的自动化的、高级的功能你需要学习很多的东西，而且它的教程一上来就是以这种过于完整的例子进行展示，自然会让你觉得很麻烦。不过看了我的讲解之后，是不是觉得还是挺简单的。那么我们就先以无数据库的方式进行下去，一点点地发掘 Django 的功能特性吧。

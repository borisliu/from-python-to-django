# Django Step by Step (五)
========================

## 1. 引言

其实本教程以展示基本概念为已任，对于一些高级的话题我也在不停地学习中，希望能有所展示。让我们一起学习吧。

在了解了基本的 Django 开发的过程及 Django 的一些基本特性之后，越来越多的东西在等着我们。现在我们就学习一下 session 吧。 session 可以翻译为“会话”，做过web的可能都知道。它就是为了实现页面间的数据交换而产生的东西，一般有一个 session_id ，它会保存在浏览器的 cookie 中，因此如果你的浏览器禁止了 cookie ，下面的试验是做不了的。

在 Django 中的 session 也非常简单，它就存在于 request 对象的 session 属性中。你可以把它看成一个字典就可以了。

下面我们做一个非常简单的功能：首先当用户进入某个页面，这个页面会显示一个登录页面，上面有一个文本框用来输入用户名，还有一个提交按钮用来提交数据。当用户输入用户名，然后点提交，则显示显示用户已经登录，并且打印出用户的姓名来，同时还提供一个“注销”按钮。然后如果用户再次进入这个页面，则显示同登录成功后的页面。如果点击注销则重新进入未登录的页面。

## 2. 创建 login.py

```
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    username = request.POST.get('username', None)
    if username:
        request.session['username'] = username
    username = request.session.get('username', None)
    if username:
        return render_to_response('login.html', {'username':username})
    else:
        return render_to_response('login.html')

@csrf_exempt
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")
```

有些复杂了吗？没关系，让我解释一下。这里有两个方法： login() 和 logout() 。 login() 用来提供初始页面、处理提供数据和判断用户是否登录。而 logout() 只是用来从 session 中删除用户名，同时将页面重定向到 login 画面。这里我仍然使用了模板，并且根据传入不同的字典来控制模板的生成。是的，因为 Django 的模块支持条件判断，所以可以做到。

在 login() 中的判断逻辑是：

*   先从 POST 中取 username (这样 username 需要由模板的 form 来提供)，如果存在则加入到 session 中去。加入 session 很简单，就是一个字典的 Key 赋值。
*   然后再从 session 中取 username ，有两种可能：一种是上一步实现的。还有一种可能是直接从以前的 session 中取出来的，它不是新产生的。而这里并没有细分这两种情况。因此这个判断其实对应两种页面请求的处理：一种是提交了用户姓名，而另一种则是处理完用户提交姓名之后，用户再次进入的情况。而用户再次进入时，由于我们在前面已经将他的名字保存在 session 里面了，因此可以直接取出来。如果 session 中存在，则表示用户已经登录过，则输出 login.html 模板，同时传入了 username 字典值。而如果 session 中不存在，说明用户从来没有登录过，则输出 login.html 模板，这次不带值。
    
因此对于同一个 login.html 模板传入的不同值，后面我们会看到模板是如何区分的。

在 logout() 中很简单。先试着删除 session ，然后重定向页面到 login 页面。这里使用了 HttpResponseRedirect 方法，它是从以前我们看到的 HttpResponse 派生来的子类。更多的派生子类和关于 response 的内容要参考 [Request and response objects](http://www.djangoproject.com/documentation/request_response/) 文档。

## 3. 创建 templates/login.html

```
{% if not username %}
<form method="post" action="/login/">
    用户名：<input type="text" name="username" value=""><br/>
    <input type="submit" value="登录">
</form>
{% else %}
你已经登录了！{{ username }}<br/>
<form method="post" action="/logout/">
    <input type="submit" value="注销">
</form>
{% endif %}
```

整个是一个 if 语句。在 Django 模板中的 if 可以象 Python 一样使用，如使用 not , and , or 。象 if not username 表示什么呢？它表示如果 username 不存在，或为空，或是假值等等。而此时我们利用了 username 不存在这种判断。

上面的逻辑表示，如果 username 不存在，则显示一个表单，显示用户名输入文本框。如果存在，则显示已经登录信息，同时显示用户名和注销按钮。而这个注销铵钮对应于 logout() 方法。

## 4. 修改 nestest/urls.py

```
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', 'helloworld.index'),
    (r'^add/$', 'add.index'),
    (r'^list/$', 'list.index'),
    (r'^csv/(?P<filename>\w+)/$', 'csv_test.output'),
    (r'^login/$', 'login.login'),
    (r'^logout/$', 'login.logout'),

    url(r'^admin/', include(admin.site.urls)),
)
```

增加了 login 和 logout 两个url映射。

## 5. 启动 server 运行

但我要说，你一定会报错。而且我的也在报错。为什么，因为从这一刻起，我们就要进入有数据库的环境了。因为在 django 中 session 是存放在数据库中的。所以在这里要进行数据库的初始化了。

## 6. 检查 settings.py

主要修改以下地方:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

可以看到Django已经配置了默认的数据库： sqlite3 ，默认的数据库名为db.sqlite3 。我们不做修改，直接初始化数据库即可。

## 7. 初始化数据库

改了配置还不够，还要执行相应的建库、建表的操作，使用 manage.py 就可以:

```
python manage.py syncdb
```

主意：创建数据库的最后，会提示用户是否需要创建一个超级用户。

```
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no):
```

在这里选择no，我们在第七讲中再来创建这个超级用户。

## 8. 启动 server

这次再进入试试吧

```
http://localhost:8000/login/
```

从此我们要进入数据库的世界了，当然目前还没有用到，而 Django 提供的许多自动化的高级功能都是需要数据库支持的。

--------------------------------------------------

### 继续阅读[第六讲](django-step-by-step/chapter6)
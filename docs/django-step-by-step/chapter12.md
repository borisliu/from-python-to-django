# Django Step by Step (十二)

## 1 引言

如果通讯录中的记录很多，我希望有一种搜索的方法，下面就让我们加一个搜索功能吧。当然，这个搜索功能是很简单的。在 [Django](https://www.djangoproject.com) 邮件列表中看到 WorldOnline(好象是它)有一个搜索的框架，可以定义哪些模块的哪些字段要参加搜索。这样在处理时会自动将相应的信息加入到搜索数据库中进行预处理。现在这个框架并没有开放源码，而且它底层使用的搜索的东西并不是 Django 本身的。这里我只是对姓名字段进行查找。

## 2 修改 templates/address/list.html

```html
[...]
<hr>
<div id="content-main">
    <table border="0" width="500">
    <tr align="right"><td>
    <form method="GET" action="/address/search/">
    搜索姓名：<input name="search" type="text" value="{{ searchvalue }}"/>
    <input type="submit" value="提交"/>
    </form>
    </td></tr>
    </table>
    <table border="0" width="500">
    <tr align="right">
      <td>{% if has_previous %}
[...]
```

在显示分页的代码上面增加了搜索的处理。

从上面可以看到，条件输入处我增加了一个 `searchvalue` 的变量，希望在提交一个搜索后，显示页面的同时显示当前显示时使用的条件。

由于搜索结果页面也是一个列表页面，我们希望能够用[第九讲](./chapter09.md)介绍过的`generic view`来显示结果，因为列表页面的处理非常简单：

```python
class IndexView(generic.ListView):
    model = Address
    template_name = 'address/list.html'
    paginate_by = 2
```

但是这里存在一个困难：如何把搜索条件，搜索字符串与generic view 相关联呢？通过 `urls.py` 我想是不行的，因为它只从 url 解析，而且对于 QUERY_STRING 是不进行解析的(QUERY_STRING 是指： `http://example.com/add/?name=test` 中 `?` 后面的东西，也就是 `name=test` )。对于搜索条件，我会使用一个 form 来处理， `method` 会设为 `GET` ，因此生成的 url 中，查询条件正如这个例子，如： `http://localhost:8000/address/search/?search=limodou` 。这样无法变成上面所要用到的参数。

这里我们需要对generic view进行一下扩充，我们需要实现`get_queryset`和`get_context_data`这两个方法。分别用来指定结果集和模板渲染的参数，我们先来看看新的view方法怎么写：

## 3 修改 address/views.py

```python
class SearchView(generic.ListView):
    
    template_name = 'address/list.html'
    paginate_by = 2

    def get_queryset(self):
        self.name = self.request.GET['search']
        if self.name:
            return Address.objects.filter(name = self.name)
        else:
            return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchvalue'] = self.name
        return context
```

我们使用`get_queryset`方法代替了`model = Address`，这样可以更加灵活的定义返回的结果集。

我们使用`get_context_data`指定了可以传入到模板中的上下文字典。

`self.request.GET['search']` 从 GET 中得到数据，是一个方便的用法。它将得到提交的查询姓名条件，然后我们使用`filter`函数对结果进行过滤。如果存在，则生成 `extra_lookup_kwargs` 和 `extra_context` 参数，然后按 `object_list` 的要求传入。如果没有提交，则回到 address 的起始页面



因此我决定自定义一个新的 view 方法。

## 4 修改 address/urls.py

```python
from django.conf.urls.defaults import *
from newtest.address.models import Address

info_dict = {
#    'model': Address,
    'queryset': Address.objects.all(),
}
urlpatterns = patterns('',
    (r'^/?$', 'django.views.generic.list_detail.object_list',
        dict(paginate_by=10, **info_dict)),
    (r'^upload/$', 'address.views.upload'),
    (r'^output/$', 'address.views.output'),
    (r'^search/$', 'address.views.search'),
)
```

增加了一个 search 的 url 链接映射。

## 5 启动 server 测试

感觉这个通讯录也差不多了，现在让我们将其部署到 Apache 上去跑一跑吧。

但部署到 apache 时才知道，问题很多啊。主要问题如下：

- 模块名不全

   比如许多例子我都是从当前目录(newtest)下开始计算，因为在 Windows 下，Python_ 会自动将当前目录加入到 sys.path 中，因此直接使用 address.* 之类的不会出错，但在 Apache 下需要使用 newtest.address.* 这样的方式。必须按教程的方式处理。主要修改 urls.py 文件。

- 相对路径的问题

   许多使用相对路径的地方都不对了。必须使用绝对路径。不过这一点对于部署来说的确有些麻烦，好在要改动的地方不多，主要在 settings.py 中。如数据库名字(sqlite3)，模板的位置。

其它的就是要注意的地方了。

## 6 部署到 Apache 上的体验

只能说是体验了，因为我不是 Apache 的专家，也不是 mod_python 的专家，因此下面的内容只能算是我个人的配置记录，希望对大家有所帮助。

### 6.1 安装 mod_python 模块

Django 对于 Apache 使用 2.X ，对于 mod_python 使用 3.X。安装 mod_python(在windows下)倒是不麻烦。但在 Django 的邮件列表中却有人对于 mod_python 和 Apache 有所讨论，主要的问题是这些改动相对较大，比如说复载，安装需要 root 权限，要重启 Apache 等。这的确是一个要注意的问题，因此有人建议使用 FastCGI 或 SCGI 来处理(这两个都不懂啊)。

### 6.2 修改 httpd.conf 文件

```bash
Listen 127.0.0.1:8888
<VirtualHost 127.0.0.1:8888>
    <Location "/">
        SetHandler python-program
        PythonPath "['D:/project/svn/limodou/django-stepbystep/newtest'] + sys.path"
        PythonHandler django.core.handlers.modpython
        SetEnv DJANGO_SETTINGS_MODULE newtest.settings_apache
        PythonAutoReload Off
        PythonDebug On
    </Location>
    Alias /site_media d:/project/svn/limodou/django-stepbystep/newtest/newtest/media
    Alias /media C:/Python24/Lib/site-packages/Django-0.91-py2.4.egg/django/contrib/admin/media
    <Location "/site_media">
        SetHandler None
    </Location>
    <Location "/media">
        SetHandler None
    </Location>
</VirtualHost>
```

这里我使用了虚拟主机([参考文档](http://www.uplinux.com/download/doc/apache/ApacheManual/vhosts/examples.html)) 来设置。即使用一台机器，不同的端口来对应不同的服务。主要原因是我希望 Django 的服务可以从 / 开始，但我还有其它的一些东西要处理。因此不希望对其它的东西有所影响。我没有两个域名，或两个 IP ，因此采用了两个不同的端口。这只是我的一种方式。因为我在本机处理，因此 IP 是 `127.0.0.1` 。实际中你应该进行修改。

`PythonPath` 是绝对路径。 `PythonDebug` 和 `PythonAutoReload` 建议在生产时设为 Off 。这里我还设了两个别名，用来指向 `site_media` 和 `media` 目录。在 `site_media` 和 `media` 的 `Location` 中设置不进行脚本的解析。

> 上面的 media 路径是指向 Django 在 Python 上的安装目录。你完全可以将其拷贝出来，这样可能要方便得多。另外在 linux 下使用 ln 也相当的方便。

同时可以注意到 `settings` 我改为了 `settings_apache` 了。一方面将要把其中的内容有关相对路径的东西改为绝对路径，另一方面我还想保持现在的 `settings.py` 。

### 6.3 复制 settings.py 到 settings_apache.py

### 6.4 修改 settings_apache.py

将相对路径改为绝对路径。主要有：

- DATABASE_NAME 
- MEDIA_ROOT 
- TEMPLATE_DIRS 
- STATIC_PATH 

将 `DEBUG` 和 `TEMPLATE_DEBUG` 改为 `False` 。这样静态文件 serverview 就无效了。这就是为什么上面的 Apache 的配置中要配置 `site_media` 的原因。

### 6.5 测试

[http://localhost:8888/address]()

更详细的内容请参见 mod_python 文档。关于 admin 的 media 和 template 好象并不需要配置，大家有什么结果可以告诉我。

同时如果你不想每次重启 Apache 来进行测试，可以将:

```
MaxRequestsPerChild 0
```

改为:

```
MaxRequestsPerChild 1
```

## 7 后话

上面的步骤是直接把开发的东西发布到了 Apache 中去，但实际中开发与运行可能环境根本不一样，最主要可能就是数据库方面的变化，如果model变化，则有可能要编写数据切换程序。许多实际的问题都需要仔细地考虑。

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
        if self.request.GET.get('search'):
            self.name = self.request.GET['search']
            return Address.objects.filter(name = self.name)
        else:
            self.name = None
            return Address.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.name:
            context['searchvalue'] = self.name
        return context
```

我们使用`get_queryset`方法代替了`model = Address`，这样可以更加灵活的定义返回的结果集。

我们使用`get_context_data`指定了可以传入到模板中的上下文字典。

`self.request.GET['search']` 从 GET 中得到数据，是一个方便的用法。它将得到提交的查询姓名条件，如果有这个参数，那么我们使用`filter`函数对结果进行过滤。如果没有提交，则显示全部数据。


## 4 修改 address/urls.py

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', helloworld.index),
    url(r'^add/$', add.index),
    url(r'^list/$', list.index),
    url(r'^xls/(?P<filename>\w+)/$', xls_test.output),
    url(r'^login/$', login.login),
    url(r'^logout/$', login.logout),
    url(r'^wiki/', include('wiki.urls')),
    url(r'^address/', include('address.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

增加了一个 search 的 url 链接映射。

## 5 启动 server 测试

感觉这个通讯录也差不多了，现在让我们将其部署到 Apache 上去跑一跑吧。

但部署到 apache 时才知道，问题很多啊。主要问题如下：

- CentOS 7服务器默认自带的Python版本太低

CentOS 7自带的Python版本为Python2.7，我们希望能够使用最新的Python 3.6

- 相对路径的问题

   许多使用相对路径的地方都不对了。必须使用绝对路径。不过这一点对于部署来说的确有些麻烦，好在要改动的地方不多，主要在 settings.py 中。如数据库名字(sqlite3)，模板的位置。

其它的就是要注意的地方了。

## 6 部署到 Apache 上的体验

只能说是体验了，因为我不是 Apache 的专家，也不是 mod_wsgi 的专家，因此下面的内容只能算是我个人的配置记录，希望对大家有所帮助。

### 6.1 服务器安装Python 3.6

下面的操作我们都假定环境是CentOS 7的环境，您可以在阿里云、腾讯云等公有云服务商购买ECS服务器，会自动给你安装好相应的操作系统，最后给你一个root的用户名和密码。

使用你自己熟悉的SSH环境，用root用户登录即可，首先安装Python 3.6，执行下面的命令。

```bash
yum install -y python36
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python36 get-pip.py
pip install virtualenv
```

这样的话你安装的pip会默认使用Python3.6，我们顺手安装好了virtualenv环境。操作系统的Python环境不要安装太多的库文件，都放到自己应用的venv环境中，创建一个虚拟的环境。

### 6.2 安装 mod_wsgi 模块

mod_wsgi的安装有很多种方法，这里介绍的是官方推荐的办法，使用pip安装，首先需要安装http的开发包，然后使用pip安装mod_wsgi到系统的lib库中，执行下面的命令。

```bash
yum install -y http-devel python36-devel
pip install mod_wsgi
```

然后我们需要将mod_wsgi安装到apache服务器module中去。

```bash
cd /etc/httpd/modules
ln -s /usr/lib64/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so mod_wsgi.so
```

我们通过在`/etc/httpd/modules`下面创建符号链接的方式，让apache在启动的时候自动加载mod_wsgi.so。

然后我们需要在`/etc/httpd/conf.modules.d`中创建一个文件，加载mod_wsgi.so，使用`vi /etc/httpd/conf.modules.d/10-wsgi.conf`命令创建配置文件，然后录入下面的内容：

```
LoadModule wsgi_module modules/mod_wsgi.so
```

之后使用`systemctl restart httpd`重启apache服务即可。

### 6.2 创建配置文件

假定我们的django工程在/var/www/proc/newtest，那么我们应该创建`/etc/httpd/conf.d/wsgi.conf`
```bash
WSGIScriptAlias /newtest /var/www/proc/newtest/newtest/wsgi.py process-group=newtest
WSGIPythonHome /var/www/proc/newtest/venv
WSGIPythonPath /var/www/proc/newtest

<Directory /var/www/proc/newtest/newtest>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

#Deamon模式设置
WSGIDaemonProcess newtest python-home=/var/www/proc/newtest/venv python-path=/var/www/proc/newtest
WSGIProcessGroup newtest

#静态文件
Alias /newtest/robots.txt /var/www/proc/newtest/static/robots.txt
Alias /newtest/favicon.ico /var/www/proc/newtest/static/favicon.ico

Alias /newtest/media/ /var/www/proc/newtest/media/
Alias /newtest/static/ /var/www/proc/newtest/static/

<Directory /var/www/proc/newtest/static>
Require all granted
</Directory>

<Directory /var/www/proc/newtest/media>
Require all granted
</Directory>
```

`WSGIPythonHome` 是Python运行环境的绝对路径，这里指向我们virtualenv的目录

这里我还设了两个别名，用来指向 `media` 和 `static` 目录。在 `media` 和 `static` 的 `Location` 中设置不进行脚本的解析。

> 上面的 media 路径是指向 Django 在 Python 上的安装目录。你完全可以将其拷贝出来，这样可能要方便得多。另外在 linux 下使用 ln 也相当的方便。

### 6.3 测试

[http://localhost:8888/address]()

更详细的内容请参见 mod_wsgi 文档。关于 admin 的 media 和 template 好象并不需要配置，大家有什么结果可以告诉我。

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

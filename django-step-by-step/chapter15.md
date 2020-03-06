# Django Step by Step (十五)

## 1 引言

在 [Ajax](https://zh.wikipedia.org/wiki/AJAX) 的试验中，你会看到有一些是用英文写的。下面就让我们学习如何将应用改为支持 i18n 处理的吧。在本讲中我会讲述我实现的过程，同时对一些问题进行讨论。 [Django](https://www.djangoproject.com/) 中 i18n 的实现过程:

### 1.1 在程序和模板中定义翻译字符串

在程序中就是使用 `_()` 将要翻译的字符串包括起来。这里有几种做法，一种是什么都不导入，这样就使用缺省的方式，另一种是导入 Django 提供的翻译函数。特别是 Django 提供了 Lazy 翻译函数，特别可以用在动态语言的切换。在模板中分几种情况：

可以使用 `{% trans %}` 标签。它用来翻译一句话，但不能在它中间使用模板变量。 
如果是大段的文本，或要处理模板变量，可以使用 `{% blocktrans %}{% endblocktrans %}` 来处理。 
Django 还支持简单的 Javascript 的 i18n 的处理，但有兴趣自已去看吧。

### 1.2 生成 po 文件

定义好翻译串之后使用 `bin/make-messages.py` 来生成 po 文件。

Django 支持多层次的处理。比如在整个 Django 的源码项目，在某一个工程，在某一个应用。在不同层次去实现 i18n 时，需要在不同的层次的根目录去执行 `make-messages.py` 。那么可以将 `make-messages.py` 拷贝到相应的目录去执行，特别是在你的工程或应用中。在执行 `make-messasges.py` 时，需要你预先创建 `conf/locale` 或 `locale` 目录，而 `make-messasges.py` 是不会自动为你创建的。那么 `conf/locale` 多用在源码中，象 Django 的源码就是放在 `conf/locale` 中的。 **但在运行时，对于自已的项目和应用却是从 ``locale`` 中来找的 。**因此还是建议你创建 `locale` 来存放 po 文件。

第一次执行时:

```bash
make-messages.py -l zh_CN
```

这时会生成 `locale/zh_CN/LC_MESSAGES/django.po` 和 `django.pot` 两个文件。

然后你就可以开始翻译了。翻译完成之后，首先要执行类目->设置，将缺省的参数修改一下。主要是：项目名称及版本，团队，团队专用电子邮件，字符集(一般为 utf-8)。这些如果不改， poEdit 在保存时会报错。使用 poEdit 的一个好处是，在保存时它会自动将 po 编译成 mo 文件。

以后再更新时:

```bash
make-messasges.py -a
```

如果已经有多个语言文件，那么执行时会同时更新这些 po 文件。

## 1.3 配置

Django 有一系列的策略来实现 i18n 的功能。基本上分为静态和动态。

静态是指在 `settings.py` 中设置 `LANGUAGE_CODE` 为你想要的语言。那么这里要注意，中文的语言编码是 `zh-cn` ，但 `locale` 目录下却是 `zh_CN` 。这是为什么：其实一个是 language(zh-cn) ，一个是 locale(zh_CN) ，在 Django 的 `utils.translation.py` 中有专门的方法可以进行转换。因此在 Django 的程序中使用的是 language 的形式，在目录中却是使用 locale 的形式。一旦设为静态，则它表示是全局性质的，在所有其它的策略失效后将使用这种策略。

而动态是指在运行中对于不同的用户，不同的浏览器的支持的语言可以有不同的语言翻译文件被使用。这种方式需要在 `settings.py` 中安装 `django.middleware.locale.LocaleMiddleware` 到 `MIDDLEWARE_CLASSES` 中去。同时如果你想在实现应用中的翻译文件被使用，也要采用这种方式。

在一个请求发送到 Django 之后，如果安装了 `LocaleMiddleware` ，它会采用下面的策略：

  * 在当前用户的 session 中查找 `django_language` 键字。 
  * 如果没有找到则在 cookie 中查找叫 `django_language` 的值。 
  * 如果没有找到，则查看 `Accept-Language` HTTP 头。这个头是由浏览器发送给服务器的。 
  * 如果没有找到，则使用全局的 `LANGUAGE_CODE` 设置。 

如果你使用 FireFox 可以在 Tools->Options->Advanced->Eidt Languages 设置你所接受的语言，并且将 `zh-cn` 放在最前面。

上面讲述得还是有些粗，建议你好好阅读 i18n 的文档。

> 国际化处理的文档请参阅： [Internationalization](https://docs.djangoproject.com/en/2.0/topics/i18n/) 文档

下面开始我们的试验。

## 2 修改 ajax/views.py

```Python
#coding=utf-8
# Create your views here.
from django.http import HttpResponse

def input(request):
    input = request.REQUEST["input"]
    return HttpResponse(_('<p>You input is "%s"</p>') % input)

def json(request):
    a = {'head':(unicode(_('Name'), 'utf-8'), unicode(_('Telphone'), 'utf-8')),
        'body':[(u'张三', '1111'), (u'李四', '2222')]}
    import simplejson
    return HttpResponse(simplejson.dumps(a))
```

这里对所有英文都使用 `_()` 进行了封装。但对于 Json 方法，这里我使用 `unicode(_('Name'), 'utf-8')` 进行了转换。

## 3 修改 settings.py

增加 `LocaleMiddleware`

```Python
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
```

这里在文档中对于 `LocaleMiddleware` 的顺序有要求，要求排在 `SessionMiddleware` 之后，但在其它的 Middleware 之前。

> 话虽如此，但我感觉目前顺序影响不大，也许只是个人感觉吧。

## 4 创建 ajax/locale 目录

## 5 拷贝 make-messasges.py 到 ajax 目录下

## 6 执行 make-messasges.py

```bash
cd ajax
make-message.py -l zh_CN
```

## 7 使用 poEdit 翻译 django.po 文件

按上面说的先更新 pot 文件，然后修改缺省的参数，再保存。

> 如果你没有 poEdit，或不在 Windows 平台下，那么只好自已去想办法了。同时这里 make-message.py 还需要 Windows 下的 xgettext 工具。可以在 [http://code.djangoproject.com/wiki/Localization]() 找到说明。

这里我没有演示模板的处理。因为 Ajax 所用到的模板没有放在 `ajax` 目录下，而是放在 `templates` 目录下。因此，如果想支持 i18n 的话，目录的布置是一个问题。所以不再试验了。

## 8 启动 server 测试

是不是都是中文了呢？如果不是，看一看是否浏览器没有设置成接受 `zh-cn` 。

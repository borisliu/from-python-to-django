# Django Step by Step (三)

## 1   引言

经过前几节的学习，我想大家应该比较熟悉 Django 的大致开发流程：

* 增加 view 方法 
* 增加模板 
* 修改 urls.py 

就是这样。剩下的就是挖掘 Django 提供的其它的能力。在我们还没有进入模型(model)之前还是再看一看外围的东西，再更进一步体验 Django 吧。

在 Django 中我看到了一个生成 csv 格式的文档(Outputting CSV dynamically)，非常好，它没有数据库，正好用来做演示。

更进一步，现在我的需求就是提供 excel 格式文件的下载。

我们会在原来 list(表格) 例子基础上进行演示，步骤就是上面的流程。

## 2   修改 templates/list.html

在文件最后增加:

```html
<p><a href="/xls/address/">Excel格式下载</a></p>
```

它将显示为一个链接，它所指向的链接将用来生成 Excel 文件。

## 3   在newtest下增加 xls_test.py

```python
from django.http import HttpResponse
from django.template import loader, Context

address = [
    ('张三', '地址一'),
    ('李四', '地址二')
    ]

def output(request, filename):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % filename

    t = loader.get_template('xls.html')
    c = Context({
        'data': address,
    })
    response.write(t.render(c))
    return response
```

这里使用的东西多了一些。这里没有 `render_to_response` 了，而是演示了一个完整的从头进行模板解析的处理过程。为什么需要这样，因为我们需要修改 `response` 对象的值，而 `render_to_response` 封装了它使得我们无法修改。从这里我们也可以看到，在调用一个方法时， Django 会传入一个 `request` 对象，在返回时，你需要将内容写入 `response` ，必要时修改它的某些属性。更详细的建议你参考 django 所带的 request_response 文档，里面详细描述了两个对象的内容，并且还可以在交互环境下进行测试，学习非常方便。

这里 `address` 不再是字典的列表，而是 tuple 的列表。让人高兴的是， Django 的模板除了可以处理字典，还可以处理序列，而且可以处理序列中的元素。一会在模板定义中我们会看到。

这里 `output()` 是我们希望 Django 调用的方法，不再是 `index()` 了。(不能老是一样的呀。)而且它与前面的 `index()` 不同，它带了一个参数。这里主要是想演示 url 的参数解析。因此你要注意，这个参数一定是放在 url 上的。它表示输出文件名。

```python
response = HttpResponse(mimetype='application/ms-excel')
response['Content-Disposition'] = 'attachment; filename=%s.xls' % filename
```

这两行是用来处理输出类型和附件的，以前我也没有用过，这回也学到了。它表明返回的是一个Excel格式的文件。

```python
t = loader.get_template('xls.html')
c = Context({
    'data': address,
})
response.write(t.render(c))
```

这几行就是最原始的模板使用方法。先通过 `loader` 来找到需要的模板，然后生成一个 template 对象，再生成一个 `Context` 对象，它就是一个字典集。然后 `t.render(c)` 这个用来对模板和提供的变量进行合并处理，生成最终的结果。最后调用 `response.write()` 将内容写入。

## 4   增加 templates/xls.html

```html
<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
      <table>
        {% for row in data %}
        <tr>
            <td>{{ row.0|addslashes}}</td>
            <td>{{ row.1|addslashes}}</td>
        </tr>
        {% endfor %}
  </body>
</html>```

使用了一个 for 循环。这里 `data` 与上面的 `Context` 的 `data` 相对应。因为 `data` 是一个列表，它的每行是一个 tuple ，因此 `row.0`, `row.1` 就是取 tuple 的第一个和第二个元素。`|` 是一个过滤符，它表示将前一个的处理结果作为输入传入下一个处理。因此 Django 的模板很强大，使用起来也非常直观和方便。 `addslashes` 是 Django 模板内置的过滤 Tag ，它用来将结果中的特殊字符加上反斜线。

同时我们注意到，每个 `{{}}` 前后都有一个双引号，这样就保证每个字符串使用双引号引起来。然后在第一个与第二个元素之间还使用了逗号分隔。最后 `endfor` 在下一行，表示上面每行模板后有一个回车。

Django 还允许你自定义 Tag ，在 The Django template language: For Python programmers 文档中有描述，其实是很简单的。

## 5   修改 urls.py

```python
from django.conf.urls import url
from django.contrib import admin
from . import helloworld, add, list, xls_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', helloworld.index),
    url(r'^add/$', add.index),
    url(r'^list/$', list.index),
    url(r'^xls/(?P<filename>\w+)/$', xls_test.output),
]
```

增加了 xls 的 url 映射。

上面的正则表达式有些复杂了，因为有参数的处理在里面。 `(?P<filename>\w+)` 这是一个将解析结果起名为 `filename` 的正则表达式，它完全符合 Python 正则表达式的用法。在最新的 Django 中，还可以简化一下： `(\w+)` 。但这样需要你的参数是按顺序传入的，在一个方法有多个参数时一定要注意顺序。

还记得吗？我们的链接是写成 `/xls/address/` ，因此上面实际上会变成对 `xls.output(filename='address')` 的调用。

## 6   启动 server

看一下结果吧。点击链接，浏览器会提示你保存文件的。

很简单吧。但这里面的内容其实也不少，而且许多地方都有很大的扩展空间。

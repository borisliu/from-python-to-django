# Django Step by Step (十四)

## 1 引言

[Ajax](https://zh.wikipedia.org/wiki/AJAX) 因为大量地使用了 Javascript ，而调试 Javascript 的确不是件容易的事，在这方面只有不停地测试，还要靠耐心。而且 Ajax 本身可能还有一些安全方面的东西需要考虑，但这些话题需要你自已去学习了。

在试验了简单的 Html 返回片段之后，让我们再体验一下 Json 的应用吧。为了使用 Json ，我下载了 [simplejson](https://simplejson.readthedocs.io/en/latest/) 模块。我下载的是 1.1 版本。还可以使用 easy_install 来安装。

如何使用 simplejson 在它自带的文档有示例很简单，下面我们就用它来试验 Json 的例子。

我将在上一例的基础之上，增加一个按钮，这个按钮点击后，会发送一个请求(不带 Json 信息)，然后 [Django](https://www.djangoproject.com/) 会返回一个 Json 格式的表格数据，分为头和体两部分。然后前端动态生成一个表格显示在 `output` 层中。

## 2 修改 ajax/views.py

```Python
#coding=utf-8
# Create your views here.
from django.http import HttpResponse

def input(request):
    input = request.REQUEST["input"]
    return HttpResponse('<p>You input is "%s"</p>' % input)

def json(request):
    a = {'head':('Name', 'Telphone'), 'body':[(u'张三', '1111'), (u'李四', '2222')]}
    import simplejson
    return HttpResponse(simplejson.dumps(a))
```

> 由于使用了汉字，前面的 coding=utf-8 一定要加上。

`json()` 是新加的方法。 a 是一个字典，它会被封装为 Json 的格式。这里还使用了汉字，但使用了 unicode 的表示。我发现 simplejson 在处理非 ascii 码时会自动转为 unicode ，但不正确，因此我直接使用了unicode。因此我希望浏览器可以根据这个数据生成表格。

## 3 修改 templates/ajax/ajax.html

```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <title>Ajax Test</title>
        <script type="text/javascript" src="/site_media/MochiKit.js"></script>
        <script type="text/javascript" src="/site_media/ajax_test.js"></script>
    </head>
    <body>
        <h1>
            Ajax 演示
        </h1>
        <div>
        <form id="form">
        输入：<input type="text" name="input"/>
        <input id="submit" type="button" value="提交" />
        <input id="json" type="button" value="JSON演示" />
        </form>
        </div>
        <div id="output"></div>
    </body>
</html>
```

这里只是增加了一个按钮， id 是 `json` 。它将用来触发 Ajax 请求。

## 4 修改 media/ajax_test.js

```Javascript
function callJson(){
    var d = loadJSONDoc('/ajax/json/');
    d.addCallbacks(onSuccessJson, onFail);
}
row_display = function (row) {
    return TR(null, map(partial(TD, null), row));
}
onSuccessJson = function (data){
    var output = $("output");
    table = TABLE({border:"1"}, THEAD(null, row_display(data.head)),
        TBODY(null, map(row_display, data.body)));
    replaceChildNodes(output, table);
    showElement(output);
}
function init() {
    var btn = $("submit");
    btn.onclick = submit;
    var output = $("output");
    hideElement(output);
    var btn = $("json");
    btn.onclick = callJson;
}
```

在最后一行 `addLoadEvent(init);` 前加入上面的内容。对于 id 为 `json` 的按钮的事件绑定方式与上一例相同，都是在 `init()` 中进行的。在 `callJson()` 中进行实际的 Json 调用，这次使用了 [MochiKit](https://mochi.github.io/mochikit/) 提供的 `loadJSONDoc()` 函数，它将执行一个 url 请求，同时将返回结果自动转化为 Json 对象。一旦成功，将调用 `onSuccessJson()` 函数。在这里将动态生成一个表格，并显示出来。

表格的显示使用了 MochiKit 的 DOM 中的示例的方法。 `row_display()` 是用来生成一行的。`TBODY` 中使用map来处理数组数据。在 MochiKit 中有许多象 [Python](https://www.python.org/) 内置方法的函数，因为它的许多概念就是学的 Python 。 `replaceChildNodes()` 是用来将生成的结果替换掉 `output` 元素的内容。

## 5 修改 urls.py

```Python
(r'^ajax/json/$', 'newtest.ajax.views.json'),
```

增加上面一行。这样就增加了一个 Json 的 url 映射。

## 6 启动 server 进行测试

这里两个演示共用了 output 层作为显示的对象，你可以同时试一试两个例子的效果。

不过这里有一个问题：只有返回时使用了 Json 。的确是，这样是最简单处理的情况。因为 Json 可以包装为字符串，这样不用在底层进行特殊处理。如果请求也是 Json 的，需要设计一种调用规则，同时很有可能要实现 MiddleWare 来支持。在 Django 中的确有人已经做过类似的工作。不过我目前没有研究得那么深，因此只要可以处理返回为 Json 的情况已经足够了。而且 Django 也正在进行 Ajax 的支持工作，不过可能是以 [dojo](http://dojotoolkit.org/) 为基础的，让我们拭目以待吧。

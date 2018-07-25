# Django Step by Step (十三)

## 1 引言

经过一段时间的学习，我想大家对于 [Django](https://www.djangoproject.com/) 的一些基础的东西已经有所了解，但 Django 本身的内容不仅仅如此，它还在发展中，还有许多的专题是我还没有向大家介绍的。因此，随着我和大家一同地学习，我会继续向大家介绍一些更高级的话题。

随着对于web的了解越来越多，我对于 web 上的开发也越来越有兴趣。的确，在实际的工作中我也发现，现在越来越强调团队的管理，许多事情单纯搞一两个人是很困难的，因此如何提高团队工作的一致性和方便性越来越重要，比如：在我所在的项目组，有一些统计信息需要每个人提供，然后进行汇总。目前还是采用手工的方式，这种方式的确简单，但不能自动地进行管理，也不利于以后的归档处理。因此我很希望做成 web 的应用，让每个人可以自由创建项目，提交数据。但就是这样的一个简单的工作，也不是非常简单的事情。如何快速对 Django 加深了解，如何提高开发效率，如何更有效地利用 web 是我更关心的，而不仅仅是做出一个可用的应用来。这包括一系列的 NewEdit 的扩展，及其关知识的积累。

特别让我感兴趣，并且可以极大的提高用户体验的一种 web 技术就是 [Ajax](https://zh.wikipedia.org/wiki/AJAX) 了。它是什么？它是一种技术的总称，包括了 Html, CSS, XML, Javascript 等与 web 相关技术的合集，在我以前的 Blog 也有一些涉及，但那时关注的焦点不在 web 上。现在有机会和时间好好地了解了一下，特别是在 Django 中已经做为实现的目标正在逐步地开展起来，只不过目前还没有可用的东西呈现出来。

[Ajax](https://zh.wikipedia.org/wiki/AJAX)技术实际上就是利用了浏览器提供的XMLHttpRequest函数(XHR)，在不重新加载网页的情况下，可以异步从后台读取数据改变网页内容的一项技术。AJAX即Asynchronous JavaScript and XML（异步JavaScript和XML）

随着近些年前端技术的不断发展，JavaScript也在不断进化。现在我们使用前端库和React、Angular、Vue等框架构建了动态的网站。AJAX的概念也经历了重大变化，因为现代异步JavaScript调用涉及检索JSON而不是XML。有很多库允许你从客户端应用程序对服务器进行异步调用。有些进入到浏览器标准，有些则有很大的用户基础，因为它们不但灵活而且易于使用。有些支持promises，有些则使用回调。

Vue2.0之后，尤雨溪推荐大家用[axios](https://github.com/axios/axios)替换JQuery ajax，让[axios](https://github.com/axios/axios)进入了很多人的目光中。[axios](https://github.com/axios/axios)本质上也是对原生XHR的封装，只不过它是Promise的实现版本，符合最新的ES规范。

下面就让我以 [axios](https://github.com/axios/axios) 为基础来向大家介绍一下如何在 Django 中使用它，使用一些简单的 Ajax 技术。

首先让我们关心一下 Ajax 与 Django 的关系。其实 Ajax 本身包含许多的内容，它有浏览器端的显示技术，有与后台通讯的处理，因此与 Django 有关系的其实只有与后台交互那块东西。这样，更多的关于前端显示的技术，如：显示特效，这些都属于 CSS, Javascript的内容，而这些与 [Python](https://www.python.org/) 本身的关系也不大，因此你还需要掌握这些东西才可以做得更好。也许有机会会有专题和学习和介绍这些方面的东西。

下面的试验主要关注的是前端与后端的交互，也就是如何实现浏览器与 Django 交互，体验不进行页面的刷新(这是Ajax最大的好处，一切都好象在本地进行一样)。

就目前来说， Ajax 与后台交互都是通过浏览器提供的 `XMLHttpRequest` 对象来实现的。这个对象支持同步和异步的调用，但由于 Javascript 本身没有多线程这个东西，因此为了不阻塞浏览器，一般都采用异步方式来调用，而这也是一般的 Ajax 框架提供了默认方式。就目前来说，交互数据也有多种格式，比如：XML, Json , 纯文本/Html。 XML 不用说了，但一般采用 http 协议的 web server 是无法直接支持，因此需要进行转换。同时在浏览器你要同时进行XML的解析，不是非常方便。 Json 是一种数据表示格式，它非常象 Python 的数据类型。而且它只有数据，没有任何的格式，因此数据传输量非常小。再加上处理起来也很方便，在传输上可以直接转换为文本，然后再转换成不同语言的数据结构即可。对于 Python 是非常方便。再有就是文本/Html方式，一种是自定义格式，通过转化为文本进行处理，另一种就是直接使用 html 标记。前一种需要自行做扩展，后一种则是最方便。下面我们将先使用 html 方式，然后再使用 Json 来进行试验。

我设计了一个非常简单的例子：提供一个输入框，用户输入文本，然后点提交，直接在下面显示后台返回的结果。因为我不是 Javascript , CSS 的专家，可能有不对的地方。

## 2 创建 Ajax 应用

```bash
python manage.py startapp ajax
```

## 3 修改 ajax/views.py

```Python
# Create your views here.
from django.http import HttpResponse

def input(request):
    input = request.REQUEST["input"]
    return HttpResponse('<p>You input is "%s"</p>' % input)
```

从这里可以看出，我需要一个 input 字段，然后返回一个HTML的片段。

## 4 创建 templates/ajax 目录

## 5 创建 templates/ajax/ajax.html

```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <title>Ajax Test</title>
        <script src="https://cdn.jsdelivr.net/npm/jquery/dist/jquery.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.js"></script>
        <script src="/static/ajax_test.js"></script>
    </head>
    <body>
        <h1>
            Ajax 演示
        </h1>
        <div>
        <form id="form">
        输入：<input type="text" id="name" name="input"/>
        <input id="submit" type="button" value="提交" />
        </form>
        </div>
        <div id="output"></div>
    </body>
</html>
```

这个模板将作为初始页面，它用来处理向后台发起请求。在这里它没有需要特殊处理的模板变量，只需要显示即可。但在这里的确有许多要说明的东西。

这是一个标准的 html 的页面，在 head 标签中，它将引入三个 js 文件： jquery.js 、 axios.js 和 ajax_test.js 。我们采用[jsdelivr](https://www.jsdelivr.com)所提供的CDN服务加载jquery.js和axios.js，这样有两个好处，一来可以保持我们始终采用最新的版本，二来也可以分担我们服务器的流量压力。从 url 上可以看出，我将会ajax_test.js放在 static 下，这个地址就是 static 目录。 

在 html 文件中有一个 form ，它的 id 是 form ，我将用它来查找 form 对象。它有一个文本输入框，还有一个按钮，但这个按钮并不是 submit 按钮。这里有许多与标准的 form 不一样的地方，没有 action, 没有 method ，而且没有 submit 按钮。为什么要这样，为了简单。以前写 HTML，CSS, Javascript 和事件之类的处理，我们一般可能会写在一起，但这样的确很乱。我们在这里尝试使用代码分离技术，而这也是目前可能流行的做法。我们在独立的 Javascript 中编写代码，在装载页面时动态地查找相应的元素，然后设置元素的一些属性，如 style ，事件代码等。而在 Html 文档中，你看到的元素中一般就只有 id , class 等内容。这样的好处可以使得处理为以后重用及优化带来方便，同时可以通过编程的方式实现批量的处理，而且也使得 Html 页面更简单和清晰。因为我要使用 Ajax 去动态提交信息，不需要真正的 form 的提交机制，我只是需要用到 form 元素中的数据而已，因此象 action, method 等内容都没有用。 id 是必须的，我需要根据它找到我想要处理的元素对象。

> 不过分离的作法是你的文件将增多，也可能不如放在一个文件中便于部署吧。这是一个仁者见仁，智者见智的作法。

`<div id="output"></div>` 它是用来显示结果的层。

整个处理过程就是：

  在装载 html 页面时，会对按钮进行初始化处理，即增加一个 `onclick` 的事件处理，它将完成 Ajax 的请求及结果返回后的处理。然后用户在页面显示出来后，可以输入文本，点击按钮后，将调用 `onclick` 方法，然后提交信息到 Django ，由 Django 返回信息，再由 Ajax 的 deferred 对象(后面会介绍)调用显示处理。

## 6 创建 static/ajax_test.js

```Javascript
function submit(){
    axios.get('/ajax/input/', {
            params: {
                input: $("#name").val()
            }
        })
        .then(function (response) {
            // handle success
            console.log(response);
            $("#output").html(response.data);
            $("#output").show();
        })
        .catch(function (error) {
            // handle error
            console.log(error);
            alert(error);
        });
}

function init() {
    $("#submit").click(function(){
        submit();
    });
    $("#output").hide();
}

$(function(){
    init();
});
```

这里有许多是 [jQuery](https://jquery.com/)和[axios](https://github.com/axios/axios) 的方法。

首先让我们看 `$(function(){});` 它表示将 `init()` 函数加到 `window.onload` 的响应事件对列中。浏览器在装载完一个页面后，会自动调用 `onload` 事件处理。因此在这里是进行初始化的最好的地方。

`init()` 方法一方面完成对 id 名为 `submit` 的按钮 `onclick` 处理函数的绑定工作，另一个是将 id 为 `output` 的元素隐藏。其实不隐藏也无所谓，因为它本来就是空的，因此你也看不到东西。不过如果有其它的东西这样的处理却也不错。

`$()` 是 jQuery 提供的一个 `getElement()` 函数别名，它将根据元素的 id 来得到某个对象。

`hide()` 是隐藏某个元素。想要显示某个元素可以使用 `show()` 。

最重要的工作都在 `submit()` 这个函数中。它通过调用 axios 提供的 `get()` 函数提交一个 Ajax 请求到后台。第一个参数是请求的 url ，第二个如果有的话，应该是 Query String ，即一个 url 的 ? 后面的东西。

在执行了 `get()` 之后，结果可能当时并没有返回回来，因为这是一个异步调用。因此为了在结果回来之后做后续的处理，我还需要挂接两个异步函数，一个用来处理成功的情况，一个是用来处理失败的情况。 `then()`和`catch()` 就是做这件事的。

`then()` 在 HTTP GET请求正确返回后会被调用。 `response` 是一个对象，它有一个 `data` 属性可以使用。这里因为 Django 返回的是 Html 片段，因此我只是简单地将 `output` 对象(用于显示的 div 层)的内容进行了设置。然后调用 `show()` 来将层显示出来。

`catch()` 则只是调用 `alert()` 显示出错而已。

这里有许多 Javascript 、jQuery、axios 的东西，如果大家不了解则需要补补课了。

## 7 创建 ajax/urls.py

增加两行:

```Python
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="ajax/ajax.html")),
    url(r'^input/$', views.input),
]
```

前一个使用了 generic view 所提供的 `TemplateView.as_View` 方法可以直接显示一个模板。后一个则指向了 `views.input()` 方法，它用于在前一个页面点击按钮后与后台交互的处理。

## 8 安装 ajax 应用

修改 `settings.py`

```Python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'newtest',
    'wiki.apps.WikiConfig',
    'address.apps.AddressConfig',
    'ajax.apps.AjaxConfig',
)
```

## 9 启动 server 测试

这样你在文本框中输入内容，点击提交后就会立即在文本框的下面看到结果，而页面没有刷新，这就是 Ajax 就直接的做用。

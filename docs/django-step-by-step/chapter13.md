# Django Step by Step (十三)

## 1 引言

经过一段时间的学习，我想大家对于 [Django](https://www.djangoproject.com/) 的一些基础的东西已经有所了解，但 Django 本身的内容不仅仅如此，它还在发展中，还有许多的专题是我还没有向大家介绍的。因此，随着我和大家一同地学习，我会继续向大家介绍一些更高级的话题。

随着对于web的了解越来越多，我对于 web 上的开发也越来越有兴趣。的确，在实际的工作中我也发现，现在越来越强调团队的管理，许多事情单纯搞一两个人是很困难的，因此如何提高团队工作的一致性和方便性越来越重要，比如：在我所在的项目组，有一些统计信息需要每个人提供，然后进行汇总。目前还是采用手工的方式，这种方式的确简单，但不能自动地进行管理，也不利于以后的归档处理。因此我很希望做成 web 的应用，让每个人可以自由创建项目，提交数据。但就是这样的一个简单的工作，也不是非常简单的事情。如何快速对 Django 加深了解，如何提高开发效率，如何更有效地利用 web 是我更关心的，而不仅仅是做出一个可用的应用来。这包括一系列的 NewEdit 的扩展，及其关知识的积累。

特别让我感兴趣，并且可以极大的提高用户体验的一种 web 技术就是 [Ajax](https://zh.wikipedia.org/wiki/AJAX) 了。它是什么？它是一种技术的总称，包括了 Html, CSS, XML, Javascript 等与 web 相关技术的合集，在我以前的 Blog 也有一些涉及，但那时关注的焦点不在 web 上。现在有机会和时间好好地了解了一下，特别是在 Django 中已经做为实现的目标正在逐步地开展起来，只不过目前还没有可用的东西呈现出来。那么在 Django 的 community 的 blog 上，有人发表了一篇关于使用 [dojo](http://dojotoolkit.org/) (一个 Ajax 的库)来实现在搜索栏中实时输入信息时，可以动态显示与输入信息相匹配的blog列表的一个例子。他利用 dojo 实现了一个自定义的 widget ，但我感到这种技术对于我这种对于dojo框架不熟悉的人非常有困难。从 blog 上看，实现的过程还是有些复杂。我喜欢先从简单的东西入手。 [MochiKit](https://mochi.github.io/mochikit/) 在 Django 的 Ajax 的讨论中是另一个为大家关注的东西，最大的好处是它的文档最齐全，而且从本人的理解来说，它更简单。而 dojo 则更是提供了很多的 web UI 的控件， MochiKit 基本上没有。不过，在目前情况下我也只是希望体验一下 Ajax 技术，并且做一些简单的应用，而在简单的情况下，我认为 MochiKit 做为入门，作为简单的应用也足够了。

下面就让我以 MochiKit 为基础来向大家介绍一下如何在 Django 中使用它，使用一些简单的 Ajax 技术。

首先让我们关心一下 Ajax 与 Django 的关系。其实 Ajax 本身包含许多的内容，它有浏览器端的显示技术，有与后台通讯的处理，因此与 Django 有关系的其实只有与后台交互那块东西。这样，更多的关于前端显示的技术，如：显示特效，这些都属于 CSS, Javascript的内容，而这些与 [Python](https://www.python.org/) 本身的关系也不大，因此你还需要掌握这些东西才可以做得更好。也许有机会会有专题和学习和介绍这些方面的东西。

下面的试验主要关注的是前端与后端的交互，也就是如何实现浏览器与 Django 交互，体验不进行页面的刷新(这是Ajax最大的好处，一切都好象在本地进行一样)。

就目前来说， Ajax 与后台交互都是通过浏览器提供的 `XMLHttpRequest` 对象来实现的。这个对象支持同步和异步的调用，但由于 Javascript 本身没有多线程这个东西，因此为了不阻塞浏览器，一般都采用异步方式来调用，而这也是一般的 Ajax 框架提供了默认方式。就目前来说，交互数据也有多种格式，比如：XML, Json , 纯文本/Html。 XML 不用说了，但一般采用 http 协议的 web server 是无法直接支持，因此需要进行转换。同时在浏览器你要同时进行XML的解析，不是非常方便。 Json 是一种数据表示格式，它非常象 Python 的数据类型。而且它只有数据，没有任何的格式，因此数据传输量非常小。再加上处理起来也很方便，在传输上可以直接转换为文本，然后再转换成不同语言的数据结构即可。对于 Python 是非常方便。再有就是文本/Html方式，一种是自定义格式，通过转化为文本进行处理，另一种就是直接使用 html 标记。前一种需要自行做扩展，后一种则是最方便。下面我们将先使用 html 方式，然后再使用 Json 来进行试验。

我设计了一个非常简单的例子：提供一个输入框，用户输入文本，然后点提交，直接在下面显示后台返回的结果。因为我不是 Javascript , CSS 的专家，可能有不对的地方。

## 2 创建 Ajax 应用

```bash
manage.py startapp ajax
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
        </form>
        </div>
        <div id="output"></div>
    </body>
</html>
```

这个模板将作为初始页面，它用来处理向后台发起请求。在这里它没有需要特殊处理的模板变量，只需要显示即可。但在这里的确有许多要说明的东西。

这是一个标准的 html 的页面，在 head 标签中，它将引入两个 js 文件： MochiKit.js 和 ajax_test.js 。从 url 上可以看出，我将会把它们放在 site_media 下，这个地址就是 media 目录。 MochiKit.js 你需要从 MochiKit 网站下载(最新版本为 1.2)。 MochiKit 下载后有两种格式，一种是单个文件，另一种是分散的文件。我这里使用的是单个文件。

在 html 文件中有一个 form ，它的 id 是 form ，我将用它来查找 form 对象。它有一个文本输入框，还有一个按钮，但这个按钮并不是 submit 按钮。这里有许多与标准的 form 不一样的地方，没有 action, 没有 method ，而且没有 submit 按钮。为什么要这样，为了简单，而且我发现这是 MochiKit 的开发方式。以前写 HTML，CSS, Javascript 和事件之类的处理，我们一般可能会写在一起，但这样的确很乱。在学习了一段 MochiKit 之后，我发现它的代码分离做得非常棒，而这也是目前可能流行的做法。它会在独立的 Javascript 中编写代码，在装载页面时动态地查找相应的元素，然后设置元素的一些属性，如 style ，事件代码等。而在 Html 文档中，你看到的元素中一般就只有 id , class 等内容。这样的好处可以使得处理为以后重用及优化带来方便，同时可以通过编程的方式实现批量的处理，而且也使得 Html 页面更简单和清晰。因为我要使用 Ajax 去动态提交信息，不需要真正的 form 的提交机制，我只是需要用到 form 元素中的数据而已，因此象 action, method 等内容都没有用。 id 是必须的，我需要根据它找到我想要处理的元素对象。

> 不过分离的作法是你的文件将增多，也可能不如放在一个文件中便于部署吧。这是一个仁者见仁，智者见智的作法。

`<div id="output"></div>` 它是用来显示结果的层。

整个处理过程就是：

  在装载 html 页面时，会对按钮进行初始化处理，即增加一个 `onclick` 的事件处理，它将完成 Ajax 的请求及结果返回后的处理。然后用户在页面显示出来后，可以输入文本，点击按钮后，将调用 `onclick` 方法，然后提交信息到 Django ，由 Django 返回信息，再由 Ajax 的 deferred 对象(后面会介绍)调用显示处理。

## 6 创建 media/ajax_test.js

```Javascript
function submit(){
    var form = $("form");
    var d = doSimpleXMLHttpRequest('/ajax/input/', form);
    d.addCallbacks(onSuccess, onFail);
}
onSuccess = function (data){
    var output = $("output");
    output.innerHTML = data.responseText;
    showElement(output);
}
onFail = function (data){
    alert(data);
}
function init() {
    var btn = $("submit");
    btn.onclick = submit;
    var output = $("output");
    hideElement(output);
}

addLoadEvent(init);
```

这里有许多是 MochiKit 的方法。

首先让我们看 `addLoadEvent(init);` 它表示将 `init()` 函数加到 `onload` 的响应事件对列中。浏览器在装载完一个页面后，会自动调用 `onload` 事件处理。因此在这里是进行初始化的最好的地方。

`init()` 方法一方面完成对 id 名为 `submit` 的按钮 `onclick` 处理函数的绑定工作，另一个是将 id 为 `output` 的元素隐藏。其实不隐藏也无所谓，因为它本来就是空的，因此你也看不到东西。不过如果有其它的东西这样的处理却也不错。

`$()` 是 MochiKit 提供的一个 `getElement()` 函数别名，它将根据元素的 id 来得到某个对象。

`hideElement()` 是隐藏某个元素。想要显示某个元素可以使用 `showElement()` 。

最重要的工作都在 `submit()` 这个函数中。它首先得到 id 为 `form` 的对象，然后调用 MochiKit 提供的 `doSimpleXMLHttpRequest()` 函数提交一个 Ajax 请求到后台。第一个参数是请求的 url ，第二个如果有的话，应该是 Query String ，即一个 url 的 ? 后面的东西。这里我只是将 form 传给它， `doSimpleXMLHttpRequest()` 会自动调用 `queryString()` (也是 MochiKit 的一个方法)来取得 `form` 中的字段信息。比如你输入了 `aaa` ，那么最终在 Django 你会看到的是:

```
/ajax/input/?input=aaa
```

`doSimpleXMLHttpRequest()` 会返回一个 deferred 对象，它是一个延迟执行对象，在执行了 `doSimpleXMLHttpRequest()` 之后，结果可能当时并没有返回回来，因为这是一个异步调用。因此为了在结果回来之后做后续的处理，我还需要挂接两个异步函数，一个用来处理成功的情况，一个是用来处理失败的情况。 `d.addCallbacks(onSuccess, onFail);` 就是做这件事的。

`onSuccess()` 在 deferred 正确返回后会被调用。 `data` 是 `XMLHttpRequest` 对象本身，它有一个 `responseText` 属性可以使用。这里因为 Django 返回的是 Html 片段，因此我只是简单地将 `output` 对象(用于显示的 div 层)的内容进行了设置。然后调用 `showElement()` 来将层显示出来。

`onFail()` 则只是调用 `alert()` 显示出错而已。

这里有许多 Javascript 和 MochiKit 的东西，如果大家不了解则需要补补课了。其中 MochiKit 的内容在它自带的例子和文档中可以查阅，特别是 MochiKit 自带了一个象 Python shell 一样的命令行解释环境可以进行测试，非常的方便。具体的看 MochiKit 网站上的 [ScreenCast](http://www.archive.org/download/MochiKit_Intro-1/MochiKit_Intro-1.mov) 可以了解。

## 7 修改 urls.py

增加两行:

```Python
(r'^ajax/$', 'django.views.generic.simple.direct_to_template',
    {'template': 'ajax/ajax.html'}),
(r'^ajax/input/$', 'newtest.ajax.views.input'),
```

前一个使用了 generic view 所提供的 `direct_to_template()` 方法可以直接显示一个模板。后一个则指向了 `views.index()` 方法，它用于在前一个页面点击按钮后与后台交互的处理。

## 8 安装 ajax 应用

修改 `settings.py`

```Python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'newtest.wiki',
    'newtest.address',
    'newtest.ajax',
    'django.contrib.admin',
)
```

## 9 启动 server 测试

这样你在文本框中输入内容，点击提交后就会立即在文本框的下面看到结果，而页面没有刷新，这就是 Ajax 就直接的做用。

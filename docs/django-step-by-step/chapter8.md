# Django Step by Step (八)
=========================

## 1. 引言

上一讲的确很长，但如果看代码你会发现，代码主要在 model 的调整中，urls.py 的工作不多，而连一行 view 的代码都没有写。是不是非常方便呢！

那么让我们来继续完善这个通讯录吧。

现在我想完成的是：

*   增加批量导入和导出功能

为什么要批量导入呢？因为一般情况下，我一定是已经有了一个通讯录文件(象以前我说过的Excel文件)，那么现在需要转到 web 上来，难道要我一条条全部手工录入吗？能不能上传文件，自动插入到数据库中去呢？那么就让我们实现一个文件上传的处理吧。

为了简化，我采用csv格式文本文件(这个文件在svn中有一个例子 data.csv ，不然就自行生成好了)。

```
abc,M,11,11,11,
bcd,M,11,11,11,
ass,M,11,11,11,
dfsdf,F,11,11,11,
sfas,F,11,11,11,
...
```

## 2. 修改 templates/address/address_list.html

```
<h1 id="title">通讯录</h1>
<hr>
<form enctype="multipart/form-data" method="POST" action="/address/upload/">
上传通讯录文件： <input type="file" name="file"/><br/>
<input type="submit" value="上传文件"/>
</form>
<table border="1">
<tr>
  <th>姓名</th>
  <th>性别</th>
  <th>电话</th>
  <th>手机</th>
  <th>房间</th>
</tr>
{% for person in object_list %}
<tr>
  <td>{{ person.name }}</td>
  <td>{{ person.gender }}</td>
  <td>{{ person.telphone }}</td>
  <td>{{ person.mobile }}</td>
  <td>{{ person.room }}</td>
</tr>
{% endfor %}
</table>
```

## 3. 修改 address/views.py

```
from django.views.generic import ListView
from address.models import Address
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import csv
import io
import sys

class AddressList(ListView):
    model = Address

@csrf_exempt
def upload(request):
    file_obj = request.FILES.get('file', None)
    if file_obj:
        buf = io.StringIO(file_obj.read().decode(sys.getfilesystemencoding()), newline = None)
        try:
            reader = csv.reader(buf)
        except:
            return render_to_response('address/error.html',
                {'message':'你需要上传一个csv格式的文件！'})
        for row in reader:
            objs = Address.objects.filter(name=row[0])
            if not objs:
                obj = Address(name=row[0], gender=row[1],
                    telphone=row[2], mobile=row[3], room=row[4])
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
                obj.room = row[4]
            obj.save()

        return HttpResponseRedirect('/address/')
    else:
        return render_to_response('address/error.html',
            {'message':'你需要上传一个文件！'})
```

这里有一个 upload() 方法，它将使用 csv 模块来处理上传的 csv 文件。首先查找姓名是否存在于数据库中，如果不存在则创建新记录。如果存在则进行替换。如果没有指定文件直接上传，则报告一个错误。如果解析 csv 文件出错，则也报告一个错误。

报造错误使用了一个名为 error 的模板，我们马上要创建。

## 4. 创建 templates/address/error.html

```
<h2>出错</h2>
<p>{{ message }}</p>
<hr>
<p><a href="/address/">返回</a></p>
```

很简单。

## 5. 修改 address/urls.py

```
from django.conf.urls import patterns, url
from address.views import AddressList

urlpatterns = patterns('',
    url(r'^$', AddressList.as_view()),
    (r'^upload/$', 'address.views.upload'),
)
```

增加一个 upload 的 url 映射。

## 6. 启动 server 测试

这样导入功能就做完了。那导出呢？很简单了，参考 csv 的例子去做就可以了。不过，并不全是这样，仍然有要修改的地方，比如 csv.html 模板，它因为写死了处理几个元素，因此需要改成一个循环处理。

## 7. 修改 templates/csv.html

```
{% for row in data %}{% for i in row %}"{{ i|addslashes }}",{% endfor %}
{% endfor %}
```

将原来固定个数的输出改为循环处理。

## 8. 修改 templates/address/address_list.html

增加一个生成导出的 csv 文件的链接

```
<h1 id="title">通讯录</h1>
<hr>
<form enctype="multipart/form-data" method="POST" action="/address/upload/">
上传通讯录文件： <input type="file" name="file"/><br/>
<input type="submit" value="上传文件"/>
</form>
<hr>
<p><a href="/address/output/">导出为csv格式文件</a></p>
<table border="1">
<tr>
  <th>姓名</th>
  <th>性别</th>
  <th>电话</th>
  <th>手机</th>
  <th>房间</th>
</tr>
{% for person in object_list %}
<tr>
  <td>{{ person.name }}</td>
  <td>{{ person.gender }}</td>
  <td>{{ person.telphone }}</td>
  <td>{{ person.mobile }}</td>
  <td>{{ person.room }}</td>
</tr>
{% endfor %}
</table>
```

## 9. 修改 apps/address/views.py

```
from django.views.generic import ListView
from address.models import Address
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
import csv
import io
import sys

class AddressList(ListView):
    model = Address

@csrf_exempt
def upload(request):
    file_obj = request.FILES.get('file', None)
    if file_obj:
        buf = io.StringIO(file_obj.read().decode(sys.getfilesystemencoding()), newline = None)
        try:
            reader = csv.reader(buf)
        except:
            return render_to_response('address/error.html',
                {'message':'你需要上传一个csv格式的文件！'})
        for row in reader:
            objs = Address.objects.filter(name=row[0])
            if not objs:
                obj = Address(name=row[0], gender=row[1],
                    telphone=row[2], mobile=row[3], room=row[4])
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
                obj.room = row[4]
            obj.save()

        return HttpResponseRedirect('/address/')
    else:
        return render_to_response('address/error.html',
            {'message':'你需要上传一个文件！'})

def output(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'address.csv'
    writer = csv.writer(response)    
    writer.writerow(['姓名', '性别', '电话', '手机', '房间'])  
    objs = Address.objects.all()  
    for obj in objs:  
        writer.writerow([obj.name, obj.gender, obj.telphone,    
                         obj.mobile, obj.room])  
    return response
```

在这里我们使用csv的writer函数构造了一个writer，然后利用writerow函数输出每一样数据到csv文件。最后返回response对象。

## 10. 修改 address/urls.py

```
from django.conf.urls import patterns, url
from address.views import AddressList

urlpatterns = patterns('',
    url(r'^$', AddressList.as_view()),
    (r'^upload/$', 'address.views.upload'),
    (r'^output/$', 'address.views.output'),
)
```

增加了对 output 方法的 url 映射。

## 11. 启动 server 测试

下载的address.csv有乱码？嗯，我这里也有。这是由于Python3内码为utf-8，而HttpResponse函数默认输出也是utf-8编码的。而Windows默认的文件编码为GB18030，所以你会看到乱码。解决这个问题有两个途径：

* 让Excel可以识别UTF-8编码的CSV
* 直接输出GB18030编码的CSV

这里我们采用第二种方法，我们需要继承一下HttpResponse类，然后修改内置的_charset，最后使用我们自己定制的GbkHttpResponse类来完成输出即可。

在output函数前面增加GbkHttpResponse类的定义。

```
class GbkHttpResponse(HttpResponse):
    def __init__(self,content=b'',*args,**kwargs):
        super(GbkHttpResponse,self).__init__(content=content,*args,**kwargs)
        self._charset = "GBK"

```

然后修改output函数的第一行，改为：

```
    response = GbkHttpResponse(mimetype='text/csv')
```

再次启动server测试，是不是看到中文了？

--------------------------------------------------

### 继续阅读[第九讲](django-step-by-step/chapter9)
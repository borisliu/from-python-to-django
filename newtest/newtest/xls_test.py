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
    c = {
        'data': address,
    }
    response.write(t.render(c))
    return response

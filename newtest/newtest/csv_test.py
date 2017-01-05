from django.http import HttpResponse
from django.template import loader, Context

address = [
    ('张三', '地址一'),
    ('李四', '地址二')
    ]

def output(request, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % filename

    t = loader.get_template('csv.html')
    c = Context({
        'data': address,
    })
    response.write(t.render(c))
    return response

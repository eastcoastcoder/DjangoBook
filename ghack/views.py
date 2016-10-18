from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context

from django.http import Http404, HttpResponse  
import datetime

#Each view always takes an HttpRequest object as its first parameter
def hello(request):
    return HttpResponse("Hello world")
    
def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    '''
    t = get_template('dateapp/current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    '''
    return render(request, 'dateapp/current_datetime.html', {'current_date': now})
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    '''
    html = "In %s hour(s), it will be  %s.  " % (offset, dt)
    return HttpResponse(html)
    '''
    return render(request, 'dateapp/hours_ahead.html', {'hour_offset': offset, 'next_time': dt})
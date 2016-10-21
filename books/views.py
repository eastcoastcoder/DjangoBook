# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse  

from books.models import Book

# Connect View Classes to urls.py
#     HttpResponse(HttpRequest)
def current_url_request_path(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

# Safely deal with HttpResponse, Arguements are assignements
#     request.META.get(Success, Exception)
def ua_browser(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

# See All HTTP Headers
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'search_form.html')
    
# GET: submitting the form is request to “get” data back
# POST: submitting the form is request to change data
'''
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q'] #ensures non-empty
        if not q:
            error = True # return search_form error
        else:
            books = Book.objects.filter(title__icontains=q) #Case-insensitive
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})
'''

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q'] #ensures non-empty
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q) #Case-insensitive
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})
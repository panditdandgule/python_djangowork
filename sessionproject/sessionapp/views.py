from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def index(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index page</h1>')

def check_view(request):
    if request.session.test_cookie_worked():
        print("cookies are working properly")
        request.session.delete_test_cookies()
        return HttpResponse('<h1>Checking pages</h1>')

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);
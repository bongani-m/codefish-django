from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!', content_type='text/plain')

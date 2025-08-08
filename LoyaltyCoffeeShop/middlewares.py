from django.http import HttpResponseRedirect
import os
from dotenv import load_dotenv
load_dotenv()

class PrivateUrls:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        published_urls = [
            '/auth/register/',
            '/auth/login/',
            '/auth/password-reset/',
            '/about/',
            '/contact/',
            '/',
            '/auth/login-master/',
            '/auth/logout/',
        ]
        if request.path not in published_urls and not request.session.get('user') and not request.session.get('master'):
            return HttpResponseRedirect('/auth/login/')
        response = self.get_response(request)
        return response

class MasterUrls:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        master_urls = [
            '/worker/dashboard/',
            '/worker/order/',
            '/worker/order/cancel/',
            '/worker/order/add/',
            '/worker/order/update/',
            '/worker/loyalty/',
            '/worker/menu/add/',
            '/worker/menu/update/',
            '/worker/menu/delete/'
        ]
        if request.path in master_urls and request.session.get('user') and not request.session.get('master') and request.session.get('master') != os.getenv('MASTER_EMAIL'):
            return HttpResponseRedirect('/auth/login-master/')
        response = self.get_response(request)
        return response
    
class HomeRedirect:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/' and request.session.get('master'):
            return HttpResponseRedirect('/worker/dashboard/')
        response = self.get_response(request)
        return response
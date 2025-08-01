from django.http import HttpResponseRedirect

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
            '/'
        ]
        if request.path not in published_urls and not request.session.get('user'):
            return HttpResponseRedirect('/auth/login/')
        response = self.get_response(request)
        return response
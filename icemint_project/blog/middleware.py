from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')

            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_url = '{login_url}?next={next_url}'.format(
                    login_url=settings.LOGIN_URL,
                    next_url=request.path_info
                )
                return HttpResponseRedirect(redirect_url)

        return self.get_response(request)

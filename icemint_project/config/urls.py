from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        settings.LOGIN_URL.lstrip('/'),
        LoginView.as_view(template_name='blog/login.html'),
        name='login',
    ),
    path(
        'logout',
        LogoutView.as_view(),
        name='logout',
    ),
    path('blog/', include('blog.urls', namespace='blog'))
]

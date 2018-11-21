from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings


def redirect_to_admin(request):
    return redirect('/admin/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^jet/', include('jet.urls', 'jet')),
    path(r'^jet/dashboard/', include('jet.dashboard.urls',
                                     'jet-dashboard')),  # Django JET URLS
    path('', redirect_to_admin)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

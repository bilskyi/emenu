from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/', permanent=True)), # for development
    path('api/', include('base.urls'), name='api'),
]

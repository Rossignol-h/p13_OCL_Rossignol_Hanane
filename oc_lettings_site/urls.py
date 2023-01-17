from django.contrib import admin
from django.urls import path, include

from . import views

# function for Sentry
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='home'),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]

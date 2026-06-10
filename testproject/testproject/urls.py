from django.urls import include, path

from django.contrib import admin

# Django Pydenticon.
import django_pydenticon.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs for Django Pydenticon.
    path('identicon/', include(django_pydenticon.urls.get_patterns())),
]

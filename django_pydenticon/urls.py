# Django imports.
from django.urls import re_path

# Application imports.
from .views import image

app_name = "django_pydenticon"

urlpatterns = [
    # View for rendering an identicon image.
    re_path(r'^image/(?P<data>.+)$', image, name="image")
    ]

def get_patterns():
    """
    Generates URL patterns for Django Pydenticon application. The return value
    of this function can be used directly by the django.urls.include function.

    The application namespace is set to "django_pydenticon", which is also used
    as the default instance namespace. An alternative instance namespace can be
    specified by passing the namespace argument to django.urls.include, for
    example:

      re_path(r'^identicon/', include(get_patterns(), namespace="myidenticon"))

    Returns:

      Tuple consisting out of URL patterns and application namespace.
    """

    return urlpatterns, "django_pydenticon"

Release notes
=============

0.4.0
-----

Update introduces support for Django 3.2 through 4.2.

* Minimum requirement for Django is now 3.2. Python 3.8 or newer is required.
* URL patterns now use ``django.urls.re_path`` instead of the
  ``django.conf.urls.url`` function that was removed in Django 4.0.
* The URL configuration module now defines ``app_name``, so the application
  can be included with ``include('django_pydenticon.urls')``.
* ``django_pydenticon.urls.get_patterns`` no longer accepts the ``instance``
  argument and now returns a 2-tuple suitable for ``django.urls.include``.
  Custom instance namespaces should be passed via the ``namespace`` argument
  of ``django.urls.include`` instead.
* The bundled test project has been updated to the modern Django settings and
  URL configuration style.

0.2
---

Update introduces support for Django 1.8+ and some documentation improvements.

New features:

* `DJPYD-7: Update application for use in Django 1.8, 1.9, and Django 1.10
  <https://projects.majic.rs/django-pydenticon/issues/DJPYD-7>`_

  Minimum requirement for Django is now 1.8.x. Fixes are compatible with Django
  1.9.x and 1.10.x as well.

Enhancements:

* `DJPYD-8: Update Pydenticon requirement to version 0.3
  <https://projects.majic.rs/django-pydenticon/issues/DJPYD-8>`_

  Introduced explicit dependency on Pydenticon 0.3, which also introduces
  ability to handle transparency in PNGs.

0.1
---

Initial release of Django Pydenticon. Implemented features:

* Serving of identicons through designated URL.
* User data for generating identicons passed via URL.
* Sane configuration defaults for identicon generator for zero-configuration.
* Ability to set parameters of generated identicons.
* Ability to override some of the identicon generation attributes per-request
  via *GET* parameters.
* Full documentation covering installation, usage, privacy. API reference
  included as well.

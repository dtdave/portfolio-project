import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# from whitenoise.django import DjangoWhiteNoise

BASE_DIR = os.path.dirname(__file__)


settings.configure(
    DEBUG=True,
    SECRET_KEY='4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh',

    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
         'django.contrib.staticfiles',
    ],
    MIDDLEWARE=[
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],

    ALLOWED_HOSTS=['127.0.0.1', '0.0.0.0', 'calm-oasis-52851.herokuapp.com',],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
            ],

        },
        ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR, 'static')
    ],
    STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles'),
    STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage',

)


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='aboutpage'),
]

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

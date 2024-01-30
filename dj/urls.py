"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from autocomplete.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #------------Pizza -----------------
    # path('', home),
    # path('login/', login_page, name='login'),
    # path('register/', register, name='register'),
    # path('add_cart/<p_uid>/', add_cart, name="add_cart"),
    # path('cart', cart, name="cart"),
    # path('remove_cart_item/<cart_item_uid>',remove_cart_item, name="remove_cart_item"),
    # path('orders', orders, name='orders')


    #-------------CompleteAuth -------------
    # path('', include('home.urls'))

    # path('', include('completeauth')),
    # path('register/', RegisterAPI.as_view()),
    # path('login/', LoginAPI.as_view()),
    # path('verify/', VerifyOTP.as_view())


    #--------------autocomplete----------------
    path('get-names/', get_names),
    path('', index)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
    

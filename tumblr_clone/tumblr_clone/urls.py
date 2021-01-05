"""tumblr_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from . import settings
import debug_toolbar


from post import views as post_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='index'),
    path('account/',include('account.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.LoginPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('post/',include('post.urls')),
    path('dashboard',post_view.Dashboard.as_view(),name='dashboard'),
    path('__debug__/', include(debug_toolbar.urls)),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""ITS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from pallevelugu import views
from ITS import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^Household/',views.Det1.as_view()),
    url(r'^mem/',views.Det2.as_view()),
    url(r'^farm/',views.Det3.as_view()),
    url(r'^well/',views.Det4.as_view()),
    url(r'^crop/',views.Det5.as_view()),
	url(r'^vill/',views.Det6.as_view()),
    url(r'^Medi/',views.Det7.as_view()),
    url(r'^Deal/',views.Det8.as_view()),
    url(r'^Mup/',views.Det9.as_view()),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

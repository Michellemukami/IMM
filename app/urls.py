"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

# auth view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/',customer_views.register,name='register'),

    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     customer_views.activate, name='activate'),
    # url(r'^activate_user/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',Activate.as_view(), name='activate_user'),
    
    # path('',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),

    # path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),

    # path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),

    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),


    # path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

    # core app will be default for all shared views and logic
    path('core/',include('core.urls')),
    path('core/',include('tatuadmin.urls')),
    path('core/',include('agent.urls')),
    path('core/',include('customer.urls')),
    
]

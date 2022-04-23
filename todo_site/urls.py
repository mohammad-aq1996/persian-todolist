"""todo_site URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('account/', include('account_app.urls')),

    path("password_reset/", auth_view.PasswordResetView.as_view(template_name='passReset.html'), name="password_reset"),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(template_name='passResetSent.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(template_name='passResetConf.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(template_name='passResetDone.html'),
        name="password_reset_complete",
    ),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

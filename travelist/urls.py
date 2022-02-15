"""travelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from account.views import AccountListView, ChangeBalance, SourcePointsView

urlpatterns = [
    path('', AccountListView.as_view()),
    path('change-balance/<user_id>', ChangeBalance.as_view(), name='change-balance'),
    path('add-sources/<user_id>', SourcePointsView.as_view(), name='add-sources'),
    path('admin/', admin.site.urls),
]

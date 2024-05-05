from django.urls import path

from siteinfo.views import main_view, about_view

app_name = "siteinfo"
urlpatterns = [
    path('main/', main_view, name = "main"),
    path('about/', about_view, name = "about"),
]


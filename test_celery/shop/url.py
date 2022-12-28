from django.urls import path

from .views import pages

app_name = "main_page"

urlpatterns = [
    path("index", pages, name="menu_in_menu"),
]
from django.urls import path

from .views import index_view, entry_create_view


urlpatterns = [
    path('', index_view, name='index'),
    path('create/', entry_create_view, name='entry_create'),
]
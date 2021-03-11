from django.urls import path

from .views import AnimalsView, delete_animal, update_animal, create_family


urlpatterns = [
    path('', AnimalsView.as_view(), name='home'),
    path('create-family/', create_family, name='create_family'),
    path('delete/', delete_animal, name='delete_animal'),
    path('update/', update_animal, name='update_animal'),
]

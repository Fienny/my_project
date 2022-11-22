from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, ProductDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
]

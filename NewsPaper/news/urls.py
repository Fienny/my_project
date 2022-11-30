from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, ProductDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('create/', PostCreate.as_view(), name='new_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]

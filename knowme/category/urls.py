from django.urls import path

from .views import create_category, category_list, get_category, update_category, delete_category

urlpatterns = [
    path("category/new/", create_category, name="create_category"),
    path("category/list/", category_list, name="category_list"),
    path("category/<str:pk>/", get_category, name="get_category"),
    path("category/<str:pk>/update/", update_category, name="update_category"),
    path("category/<str:pk>/delete/", delete_category, name="delete_category")
]

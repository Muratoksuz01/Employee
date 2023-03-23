from django.urls import path
from .views import index,liste,edit,delete
urlpatterns = [
    path("",index,name="index"),
    path("list/",liste,name="liste"),
    path("edit/<int:pk>",edit,name="edit"),
    path("delete/<int:pk>",delete,name="delete"),

]

from django.contrib import admin
from django.urls import path
from projeto.views import (
    ProjetoListView, 
    ProjetoCreateView, 
    ProjetoUpdateView, 
    ProjetoDeleteView,
    ProjetoCompleteView

)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProjetoListView.as_view(), name="projeto_list"), #list
    path("create", ProjetoCreateView.as_view(), name="projeto_create"), #form
    path("update/<int:pk>", ProjetoUpdateView.as_view(), name="projeto_update"),
    path("delete/<int:pk>", ProjetoDeleteView.as_view(), name="projeto_delete"),
    path("complete/<int:pk>", ProjetoCompleteView.as_view(), name="projeto_complete"),
]

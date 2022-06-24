from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.Postlistview.as_view(), name="all"),
    path("create/", views.Postcreateview.as_view(), name="post_create"),
    path("delete/<slug:slug>", views.Postdeleteview.as_view(), name="post_delete"),
    path("update/<slug:slug>", views.Postupdateview.as_view(), name="post_update"),
    path("read/<slug:slug>", views.Postdetailview.as_view(), name="post_detail"),

]

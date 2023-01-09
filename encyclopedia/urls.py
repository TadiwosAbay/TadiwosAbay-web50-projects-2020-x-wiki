from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.title,name="title"),
    path("wikis",views.get_entry,name="search"),
    path("wiki",views.newpage,name="new"),
    path("wikis/<str:entry>",views.editpage,name="edit"),
    path("created/<str:title>/<str:content>",views.saveNewPage,name="created"),
    path("edited/<str:title>",views.editedpage,name="edited"),
    path("random",views.randompage,name="random")
]

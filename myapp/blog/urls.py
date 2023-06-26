from django.urls import path
from . import views

# from blog.views import Index
app_name = "blog"

urlpatterns = [
    # path(pattern, mapping)
    # path("", views.index), #FBV
    # Post 목록 조회
    path("", views.List.as_view(), name="list"),  # index page를 의미함
    # Post 상세 조회
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Post Write
    path("write/", views.Write.as_view(), name="write"),
    # Post Update
    path("detail/<int:pk>/edit/", views.Update.as_view(), name="edit"),
    # Post Delete
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name="delete"),
    # Comment Write
    path("detail/<int:pk>/comment/write/", views.CommentWrite.as_view(), name="cm-write"),
    # Comment Delete
    path("detail/comment/<int:pk>/delete/", views.CommentDelete.as_view(), name="cm-delete"),
    # HashTag Write
    path("datail/<int:pk>/hashtag/write/", views.HashTagWrite.as_view(), name="tag-write"),
    # HashTag Delete
    path("detail/<int:pk>/hashtag/delete/", views.HashTagDelete.as_view(), name="tag-delete"),
]   

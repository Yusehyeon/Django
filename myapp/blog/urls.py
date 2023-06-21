from django.urls import path
from . import views

# from blog.views import Index
app_name = "blog"

urlpatterns = [
    # path(pattern, mapping)
    # path("", views.index), #FBV
    # 글 목록 조회
    path("", views.List.as_view(), name="list"),  # index page를 의미함
    # 글 상세 조회
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    # 글 작성
    path("write/", views.Write.as_view(), name="write"),
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]

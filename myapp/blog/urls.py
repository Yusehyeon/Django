from django.urls import path
from . import views

# from blog.views import Index

urlpatterns = [
    # path(pattern, mapping)
    # path("", views.index), #FBV
    path("", views.Index.as_view())  # index page를 의미함
    # 글 조회
    # 글 작성
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]

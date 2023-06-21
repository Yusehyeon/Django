from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     if request.method == "GET":
#         return HttpResponse("Index page GET")

#     # 나머지 요철
#     # 에러, 예외처리
#     return HttpResponse("No")


class Index(View):
    def get(self, request):
        # return HttpResponse("Index page GET class")

        # DB에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야해서 DA에서 "값 조회"
        # MyModel.object.all()
        post_objs = Post.objects.all()
        # cnotext = DB에서 가져온 값
        context = {"posts": post_objs}
        return render(request, "blog/board.html", context)


# write
# post - form
# def write(request):
#     if request.method == "POST":
#         # form check
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect("blog:list")

#     else:
#         form = PostForm()
#         return render(request, "blog/write.html", {"form": form})


# Django 자체의 class view 기능도 강력, 편리
# model, template_name, context_object_name,
# pagingate_by, form_class, form_valid(), get_queryset()
# django.views.generic -> ListView
class List(ListView):
    model = Post  # model
    template_name = "blog/post_list.html"  # template
    context_object_name = "posts"  # 변수 값의 이름


class Write(CreateView):
    model = Post  # model
    form_class = PostForm  # form
    success_url = reverse_lazy("blog:list")  # active sucessing send url


class Detail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

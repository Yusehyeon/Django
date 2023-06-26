from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse

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

### Post
class List(ListView):
    model = Post  # model
    template_name = "blog/post_list.html"  # template
    context_object_name = "posts"  # 변수 값의 이름


class Write(CreateView):
    model = Post  # model
    form_class = PostForm  # form
    success_url = reverse_lazy("blog:list")  # active sucessing send url


# class Detail(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"
#     context_object_name = "post"


class Update(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "content"]
    # succcess_url = reverse_lazy("blog:list")

    # initial 기능 -> form에 값을 미리 넣어주기 위해서
    def get_initial(self):
        initial = super().get_initial() # UpdateView(generic view)에서 제공하는 initial(dictionaly)
        post = self.get_object()  # pk 기반으로 객체를 가져옴
        initial["title"] = post.title
        initial["content"] = post.content
        return initial

    def get_success_url(self): 
        post = self.get_object()  # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={'pk': post.pk})


class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


class DetailView(View):
    def get(self, request, pk): # post_id : DB post_id
        # list -> object 상세 페이지 -> 상세 페이지 하나의 내용
        # pk : 하나의 인자 값
        
        # DB 방문
        # Django ORM (pk: 무조건 pk로 받아야 한다)
        post = Post.objects.get(pk=pk)
        # comment
        comments = Comment.objects.filter(post=post)
        # HAshTag
        hashtags = HashTag.objects.filter(post=post)
        # Comment Form
        Comment_form = CommentForm()
        # HashTag Form
        HashTag_form = HashTagForm()

        context = {
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': Comment_form,
            'HashTag_form': HashTag_form
        }

        return render(request, 'blog/post_detail.html', context)


### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            # user에게 comment 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 id에 해당하는 post 불러옴
            post = Post.objects.get(pk=pk)
            # comment object create,used a create method have not save
            comment = Comment.objects.create(post=post, content=content)
            return redirect('blog:detail', pk=pk)


class CommentDelete(View):
    def post(self, request, pk):
        # 지울 객체 -> 댓글 객체
        comment = Comment.objects.get(pk=pk)
        # 상세페이지로 돌아가기
        post_id = comment.post.id
        # Delete
        comment.delete()

        return redirect('blog:detail', pk=post_id)
    

### HashTag
class HashTagWrite(View):
    def post(self, request, pk): 
        # post의 pk(id)
        form = HashTagForm(request.POST)
        if form.is_valid():
            # user에게 tag 내용을 받아옴
            name = form.cleaned_data['name']
            # 해당 id에 해당하는 post 불러옴
            post = Post.objects.get(pk=pk)
            # tag object create, used a create method have not save
            hashtag = HashTag.objects.create(post=post, name=name)
            return redirect('blog:detail', pk=pk)


class HashTagDelete(View):
    def post(self, request, pk):
        # 해시태그의 pk(id)
        # Load a HashTag 
        hashtag = HashTag.objects.get(pk=pk)
        # post's pk(id) value
        post_id = hashtag.post.id
        # HashTag delete
        hashtag.delete()

        return redirect('blog:detail', pk=post_id)
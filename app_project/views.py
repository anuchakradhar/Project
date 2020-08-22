from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostProblem, Comment
from .forms import PostProblemForm, CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(ListView):
    model = PostProblem
    template_name = 'home.html'
    ordering = ['-created_date']
    paginate_by = 1

    #to get the objects for status dropdown
    def get_context_data(self, *args, **kwargs):
        # cat_menu = PostProblem.objects.values_list('status', flat = True).distinct()
        cat_menu = ('critical', 'mild', 'solved')
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class UserPostListView(ListView):
    model = PostProblem
    template_name = 'user_posts.html'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostProblem.objects.filter(creator=user).order_by('-created_date')

def StatusView(request, cats):
	category_posts = PostProblem.objects.filter(status = cats)
	return render(request, 'catagories.html', {'cats':cats, 'category_posts':category_posts})

def LikeView(request, pk):
    post = get_object_or_404(PostProblem, id= request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('problem-detail', args=[str(pk)]))


class ProblemDetailView(DetailView):
    model = PostProblem
    template_name = 'problem_detail.html'

    def get_context_data(self, *args, **kwargs):
        # cat_menu = PostProblem.objects.values_list('status', flat = True).distinct()
        cat_menu = ('critical', 'mild', 'solved')
        context = super(ProblemDetailView, self).get_context_data(*args, **kwargs)

        temp = get_object_or_404(PostProblem, id = self.kwargs['pk'])
        total_likes = temp.total_likes()

        liked = False
        if temp.likes.filter(id = self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddProblemView(CreateView):
    model = PostProblem
    form_class = PostProblemForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdateProblemView(UpdateView):
    model = PostProblem
    form_class = PostProblemForm
    template_name = 'update_post.html'
    # fields = ['title', 'problem', 'location', 'status' ]

class DeleteProblemView(DeleteView):
    model = PostProblem
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

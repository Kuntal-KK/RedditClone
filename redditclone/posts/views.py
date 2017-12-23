from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import DeleteView
from django.utils import timezone
from posts.models import Post
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create(request):
    '''title and url coming from create.html textfield'''
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = "http://" + request.POST['url']

            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error':'ERROR. Fill in all the Field'})
    else:
        return render(request,'posts/create.html')

def home(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request, 'posts/home.html',{'posts':posts})

def upvote(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')

def downvote(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home')

def user_post(request,pk):
    post = Post.objects.filter(author__id=pk).order_by('-votes_total')
    author = User.objects.get(pk=pk)
    return render(request, 'posts/user_post.html', {'post':post, 'author':author})

def deleteview(request,pk):
    post = Post.objects.get(pk=pk)
    post_pk = post.pk
    post.delete()
    post.save()
    return redirect('home')

# class PostDeleteView(LoginRequiredMixin,DeleteView):
#     model = Post
#     # after deleting any post, it will go to success_url
#     success_url = reverse_lazy('home')

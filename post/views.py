from django.shortcuts import render,redirect
from post.models import Post
from accounts.models import Profile
from post.forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all()
    profile = Profile.objects.all()

    context = {
        'posts' : posts,
        'profile':profile
    }
    return render(request, 'post/index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    
    context = {
        'post' : post
    }
    return render(request, 'post/post_detail.html', context)

@login_required
def post_create(request):
    form = PostForm()
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = Post(
                title = data['title'],
                content = data['content'],
              
            )
            new_post.save()
            return redirect('/')
    context ={
        'form': form
    }

    return render(request, 'post/post_create.html',context)

# Create your views here.

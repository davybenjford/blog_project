from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#Go and get the default crud class views
from django.views.generic import  (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)
from blog.models import Post,Comment

#reversing back once you have deleted a post
from django.urls import reverse_lazy
#Import both the form to create a post and the form to create a comment
from blog.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


#Views create the elements which populate the templates through returning information to the templates

#Page containin
class AboutView(TemplateView):
    template_name = 'about.html'

#Retrieve

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        #Field Lookups
        #Specify a sql query using a python sort of code, in this case the lte means less than or equal to
        #The full line needs to be filtered and then it should be ordered, just like sql
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#Detail of the specific post
class PostDetailView(DetailView):
    model = Post

#CRUD

#Create View
class CreatePostView(LoginRequiredMixin,CreateView):
#when youa re logged in and dont know where to go, this is where you do
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

#Update View
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


#DeleteView
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        #Field Lookups
        #Specify a sql query using a python sort of code, in this case the lte means less than or equal to
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


###################################################################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)



#Area to comment on the posts

#takes the request and the primary key which is associated
# @login_required
# def add_comment_to_post(request,pk):
#     #Get the post object of the get_object_or_404
#     #If someone has actually clicked the form
#     post = get_object_or_404(Post,pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         #if the form has been done correctly
#         if form.is_valid():
#             #form is saved in memnory
#             comment = form.save(commit=False)
#             #comment has an attribute which is post
#             comment.post = post
#             comment.save()
#             #go to the form which you have commented on
#             return redirect('post_detail',pk=post.pk)
#     else:
#         #form is equal to the comment form with no extra information
#         form = CommentForm()
#     #Passing back a rendered html with a context dictionary being the form
#     return render(request,'blog/comment_form.html',{'form':form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

#Comment approval
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


#
@login_required
def comment_remove(request,pk):
    #Gets the comment object within the request
    comment =get_object_or_404(Comment,pk=pk)
    #gets the primary key for the post associated with the comment
    post_pk = comment.post.pk
    #deletes the comment
    comment.delete()
    #sends back to detail of the post for which there was a comment
    return redirect('post_detail',pk=post_pk)

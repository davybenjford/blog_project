from django.urls import path,re_path
from blog import views

#URL patterns create the structure of the locations for the views files adding views to a certain locations

#The regular expressions means that URLs can be created with variable elements such as specific urls for different
#entries

urlpatterns = [
    #Home Page
    re_path(r'^$',views.PostListView.as_view(),name='post_list'),
    #about page
    re_path(r'^about/$',views.AboutView.as_view(),name='about'),
    #detail view
    re_path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    #Create post
    re_path(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    #Update View
    #this regex means to edit the primary key of the blog post
    re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    #delete view for the blog
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    #Drafts
    re_path(r'^draft$',views.DraftListView.as_view(),name='post_draft_list'),
    #add_comment_to_post
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    #comment approva;
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    #coment delete
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    #publish
    re_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,AuthorInterview,Suscribption
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
import random as rand

def home(request):
    context={'posts1':Post.objects.all()}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
	model=Post
	template_name='blog/home.html'
	context_object_name='posts1'
	ordering=['-date_posted']
	paginate_by=5
	


class UserPostListView(ListView):
	model=Post
	template_name='blog/user_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted') 

		 

class PostDetailView(DetailView):
	model=Post
	

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','content','genre','author']
	
	def form_valid(self,form) :
		form.instance.author=self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content']
	
	def form_valid(self,form) :
		form.instance.author=self.request.user
		return super().form_valid(form)


	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False	

		



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url="/"

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False	

		
class GenreListView(ListView):
	model=Post
	template_name='blog/genre_specific.html'
	context_object_name='posts1'


	
	
class AuthorListView(ListView):
	model=AuthorInterview 
	template_name='blog/author_interview.html'
	context_object_name='posts1'
	ordering=['-date_posted']
	paginate_by=5

	
    

	
	





def about(request):
    return  render(request,'blog/about.html')



def genre_list(request):
	return render(request,'blog/genre_list.html')


def join_team(request):
	return render(request,'blog/join_team.html')

def intro(request):
	return render(request,'blog/intro.html')


def success(request):
	return render(request,'blog/success.html')




class SuscribeView(CreateView):
	model=Suscribption
	fields=['email_id']
	success_url='success'
	
	def form_valid(self,form) :
		return super().form_valid(form)





class Genre1PostListView(ListView):
	model=Post
	template_name='blog/genre_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		
		return Post.objects.filter(genre='genre1').order_by('-date_posted') 




class Genre2PostListView(ListView):
	model=Post
	template_name='blog/genre_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		
		return Post.objects.filter(genre='genre2').order_by('-date_posted') 		





class Genre3PostListView(ListView):
	model=Post
	template_name='blog/genre_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		
		return Post.objects.filter(genre='genre3').order_by('-date_posted') 		



class Genre4PostListView(ListView):
	model=Post
	template_name='blog/genre_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		
		return Post.objects.filter(genre='genre4').order_by('-date_posted') 


class Genre5PostListView(ListView):
	model=Post
	template_name='blog/genre_posts.html'
	context_object_name='posts1'
	paginate_by=5

	def get_queryset(self) :
		
		return Post.objects.filter(genre='genre5').order_by('-date_posted') 




def random(request):
	x=Post.objects.all().count()
	x=x+1
	y=rand.randrange(2,1+x,1)
	context={'posts1':Post.objects.get(id=y)}
	return render(request,'blog/random-book.html',context)

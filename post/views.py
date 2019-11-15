# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from .models import Post, Comment, Images, Profile
from .forms import PostForm, CommentForm, EditForm
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms import modelformset_factory
from django.conf.urls.static import static
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def home(request):
	post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	is_liked = False
	paginator = Paginator(post_list, 2)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'post/home.html', {'posts': posts})



@login_required(login_url='/login/')
def filter(request):
	post_list = Post.objects.filter(author=request.user).order_by('-published_date')
	paginator = Paginator(post_list, 2)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)	  
	return render(request, 'post/filter.html', {'posts': posts})



@login_required(login_url='/login/')
def other(request):
	post_list = Post.objects.filter(published_date__lte=timezone.now()).exclude(author=request.user)
	paginator = Paginator(post_list, 2)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)	  
	return render(request, 'post/other.html', {'posts': posts})



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)    



def register(request):
	if request.method =='POST':
	  username =request.POST['username']
	  first_name = request.POST['mobile']
	  last_name = request.POST['last_name']
	  email = request.POST['email']
	  password1 = request.POST['pass']
	  password2 = request.POST['conpas']
	  if password1==password2:
	  	if User.objects.filter(username=username).exists():
	  		messages.info(request, 'Username taken')
	  		return redirect('/register/')
	  	elif User.objects.filter(email=email).exists():
	  		messages.info(request, 'Email alreday exists')
	  		return redirect('/register/')
	  	else:
	  		user =User.objects.create_user(username =username, first_name =first_name, last_name =last_name, password =password1, email=email)
	  		user.save();
	  		Profile.objects.create(user=user)
	  	return redirect('/login/')
	  else:
	  	messages.info(request, 'password not match')
	  	return redirect('/register/')
		return redirect('/')	
	else:
		return render(request, 'post/register.html', {})



def login(request):
	if request.method =='POST':
	  username =request.POST['username']
	  password1 = request.POST['pass']
	  user = auth.authenticate(username=username, password=password1)
	  if user is not None:
	  	auth.login(request, user)
	  	return redirect('/')
	  else:
	    messages.info(request, 'wrong')
	    return redirect('/login/')
	else:
		return render(request, 'post/login.html', {})  



def logout(request):
  auth.logout(request)
  return redirect('/')



def favourite_post(request):
	post = get_object_or_404(Post, id = request.POST.get('id'))
	is_favourite = False
	if request.is_ajax():
		if post.favourite.filter(id=request.user.id).exists():
			post.favourite.remove(request.user)
			is_favourite = False
		else:
			post.favourite.add(request.user)
			is_favourite = True
		context={
	  	 'post': post,
	  	 'is_favourite':is_favourite,
		}
		html = render_to_string('post/favourite.html', context, request)
		return JsonResponse({'form': html})



def favourite_post_list(request):
	user = request.user
	favourite_posts = user.favourite.all()
	context = {
	'favourite_posts': favourite_posts, 
	}
	return render(request, 'post/favourite_list.html', context )



def like_post_list(request):
	user = request.user
	likes_posts = user.likes.all()
	context = {
	'like_posts': likes_posts, 
	}
	return render(request, 'post/like_list.html', context )	


def like_post(request):
  post = get_object_or_404(Post, pk = request.POST.get('id'))
  is_liked = False
  if request.is_ajax():
	  if post.likes.filter(id=request.user.id).exists():
	  	  post.likes.remove(request.user)
	  	  is_liked = False
	  else:
	  	post.likes.add(request.user)
	  	is_liked = True
	  context={
	  	 'post': post, 
		   'is_liked':is_liked,
		   'total_likes': post.total_likes(),
		  }
	  html = render_to_string('post/like_section.html', context, request)
	  return JsonResponse({'form': html})
 


@login_required(login_url='/login/')
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post=post).order_by('id')
	is_liked = False
	is_favourite = False
	if post.likes.filter(id=request.user.id).exists():
		is_liked = True
	if post.favourite.filter(id=request.user.id).exists():
		is_favourite = True	
	if request.method =='POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			text = request.POST.get('text')
			comment = Comment.objects.create(post=post, user=request.user, text=text)
			comment.save()
			#return redirect('post_detail', pk=post.pk)
	else:
		comment_form = CommentForm()
	context={
	 'post': post, 
       'is_liked':is_liked,
       'total_likes':post.total_likes(),
       'comments':comments,
       'comment_form': comment_form,
       'is_favourite': is_favourite,
    }
	if request.is_ajax():
		html = render_to_string('post/comment.html', context, request)
		return JsonResponse({'form': html})
	return render(request, 'post/post_detail.html', context)
		

def read_more(request):
	post = get_object_or_404(Post, id = request.POST.get('id'))
	if request.is_ajax():
		context = {
		'post': post,  
		}
		html = render_to_string('post/read_more.html', context, request)
		return JsonResponse({'form': html})


@login_required(login_url='/login/')
def post_new(request):
	ImageFormset = modelformset_factory(Images, fields=('image',), extra=4, max_num = 4) 
	if request.method == "POST":	 
			  form = PostForm(request.POST)
			  formset = ImageFormset(request.POST or None, request.FILES or None)
			  if form.is_valid() and formset.is_valid():
						post = form.save(commit=False)
						post.author = request.user
						post.published_date = timezone.now()
						post.save()
						messages.success(request, '{} New Post added !!!'.format(post.title))
						for f in formset:
							try:
								photo = Images(post=post, image=f.cleaned_data['image'])
								photo.save()
							except Exception as e:
								break
						return redirect('post_detail', pk=post.pk)
	else:
				form = PostForm()
				formset = ImageFormset(queryset= Images.objects.none())
	return render(request, 'post/post_new.html', {'form': form, 'formset':formset})
         


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, '{} Post Deleted!!!!'.format(post.title))
    return redirect('home')         



@login_required(login_url='/login/')
def post_edit(request, pk):
		post = get_object_or_404(Post, pk=pk)
		ImageFormset = modelformset_factory(Images, fields=('image',), extra=4, max_num = 4)
		if request.method == "POST":
				form = PostForm(request.POST, instance=post)
				formset = ImageFormset(request.POST or None, request.FILES or None)
				if form.is_valid() and formset.is_valid():
						post = form.save(commit=False)
						post.author = request.user
						post.published_date = timezone.now()
						post.save()
						data = Images.objects.filter(post=post)						
						for index, f in enumerate(formset):
							if f.cleaned_data:
								if f.cleaned_data['id'] is None:
									photo = Images(post=post, image=f.cleaned_data['image'])
									photo.save()
								elif f.cleaned_data['image'] is None:
									photo = Images.objects.get(id=request.POST.get('form-' +str(index) +'-id'))
									photo.delete()
								else:
									photo = Images(post=post, image=f.cleaned_data['image'])
									d = Images.objects.get(id=data[index].id)
									d.image = photo.image
									d.save()
						messages.success(request, '{} Post Edited!!!!'.format(post.title))			
						return redirect('post_detail', pk=post.pk)
		else:
				form = PostForm(instance=post)
				formset = ImageFormset(queryset= Images.objects.filter(post=post))
		context={
		'form': form,
		'formset': formset,
		}		
		return render(request, 'post/post_edit.html', context )



@login_required(login_url='/login/')
def editForm(request):
	if request.method == 'POST':
		profile_form = EditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, 'Profile Updated')
	else:
		profile_form = EditForm(instance=request.user.profile)		
	return render(request, 'post/profile_edit.html', {'profile_form': profile_form})
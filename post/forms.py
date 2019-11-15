from django import forms

from .models import Post, Comment, Profile
from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm

#from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title..', 'class': 'commm', 'autocomplete':'off'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your blog..', 'class': 'commm'}))
    
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments..', 'class':'commm', 'autocomplete':'off'}))

    class Meta:
        model = Comment
        fields = ('text',)  


class EditForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)





	



	#def __init__(self, *args, **kwargs):
	#	self.fields['username'].widget.attrs.update(
	#	self.fields['first_name'].widget.attrs.update(
	#	    {'placeholder': 'City', 'class': 'form-control', 'required': 'required'})
	#	self.fields['last_name'].widget.attrs.update(
	#	    {'placeholder': 'City', 'class': 'form-control', 'required': 'required'})
	#	self.fields['email'].widget.attrs.update(
	#	    {'placeholder': 'City', 'class': 'form-control', 'required': 'required'})
	#	self.fields['password'].widget.attrs.update(
	#	    {'placeholder': 'City', 'class': 'form-control', 'required': 'required'})
	#	self.fields['confrim_password'].widget.attrs.update(
	 #   {'placeholder': 'City', 'class': 'form-control', 'required': 'required'})  


    #username = forms.CharField(widget=forms.TextInput(
    #	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
    #email = forms.CharField(widget=forms.EmailInput(
    #	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
    #first_name = forms.CharField(widget=forms.TextInput(
    #	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
    #last_name = forms.CharField(widget=forms.TextInput(
    #	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
    #password = forms.CharField(widget=forms.PasswordInput(
   # 	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
    #confrim_password = forms.CharField(widget=forms.PasswordInput(
    #	attrs={'class' : 'form-conrol' , 'placeholder' : 'Enter username'}),
    #required=True, max_length=50)
#class Userform(UserCreationForm):


    #first_name = forms.CharField(max_length=30,)
    #last_name = forms.CharField(max_length=30,)
    #username = forms.CharField(max_length=30,)
    #password1 = forms.CharField(max_length=30, widget=forms.PasswordInput,)

    #email = forms.EmailField(max_length=254,)

#class meta():
		#model = User
		#fields = ('username', 'email', 'first_name', 'last_name', 'password1')
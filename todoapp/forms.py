from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todoapp.models import Todos
class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User 
        fields=["first_name","last_name","email","username","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class TodoForm(forms.ModelForm):       
    class Meta:
        model=Todos
        fields=['task_name']
        widgets={
            'task_name':forms.TextInput(attrs={"class":"form-control"})
        }

class TodoEditForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['task_name','status']
        widgets={
            'task_name':forms.TextInput(attrs={"class":"form-control"}),
            # 'status':forms.TextInput(attrs={"class":"form-control"})
        }

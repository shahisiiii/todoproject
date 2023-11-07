from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,ListView
from todoapp.forms import SignInForm,SignUpForm,TodoForm,TodoEditForm
from django.contrib.auth.models import User
from  todoapp.models import Todos
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
        
class HomePage(TemplateView):
    template_name="home.html"

    # def get(self,request,*args,**kwargs):
    #     return render(request,'home.html')
        
class SignUp(CreateView):
    model=User
    template_name='signup.html'
    form_class=SignUpForm
    success_url = reverse_lazy('signin')

    def form_valid(self,form):
        messages.success(self.request,"Registeration successfully")
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     form=SignUpForm()
    #     return render(request,"signup.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=SignUpForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         # form.save()
    #         User.objects.create_user(**form.cleaned_data)
    #         return HttpResponse("saved")
    

class SignIn(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pass_word=form.cleaned_data.get("password")
            user=authenticate(request,username=user_name,password=pass_word)
            if user:
                login(request,user)
                msg="Login successful"
                messages.success(request,msg)
                return render(request,"signin.html")
            else:
                msg="invalid credentials"
                messages.error(request,msg)
                return render (request,"signin.html")
            
class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')

class TodoCreate(CreateView):
    model=Todos
    template_name='todocreate.html'
    form_class=TodoForm
    success_url = reverse_lazy('listtodo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=TodoForm()
    #     return render(request,'todocreate.html',{'form':form})
    
    # def post(self,request,*args,**kwargs):
    #     form=TodoForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect('home')
        
class TodoList(ListView):
    model=Todos
    template_name="todolist.html"
    context_object_name="form"
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

    # def get(self,request,*args,**kwargs):
    #     #form=Todos.objects.all()
    #     form=Todos.objects.filter(user=request.user)
    #     return render (request,'todolist.html',{'form':form})
    

class TodoEdit(UpdateView):
    model=Todos
    template_name='todoedit.html'
    form_class=TodoEditForm
    success_url = reverse_lazy('listtodo')
    pk_url_kwarg="id"

    def form_valid(self, form):
        messages.success(self.request,"edited successfuly")
        return super().form_valid(form)


    # def get (self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     data=Todos.objects.get(id=id)
    #     form=TodoEditForm(instance=data)
    #     return render(request,'todoedit.html',{'form':form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     data=Todos.objects.get(id=id)
    #     form=TodoEditForm(request.POST,instance=data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('listtodo')
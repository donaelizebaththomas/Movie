from django.shortcuts import render
from app.models import movie
from app.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     m=movie.objects.all()
#     return render (request,'home.html',{'movie':m})

class HomeView(ListView):
    model=movie
    template_name="home.html"
    context_object_name='movie'


# def viewmovie(request,d):
#     m=movie.objects.get(id=d)
#     return render (request,'viewdetails.html',{'m':m})

class Details(DetailView):
    model=movie
    template_name = "viewdetails.html"
    context_object_name='m'


# def add(request):
#         if(request.method=="POST"):             #After form submission
#             form=movieform(request.POST,request.FILES)         #creates form object with values entered by user
#             if form.is_valid():                 # check validity of data
#                 form.save()                     #if  valid form object is saved into database table Book
#                 return home(request)
#
#         form=movieform() #Empty form object
#         return render(request,'add.html',{'form':form})


class Addmovie(CreateView):
    model=movie
    template_name="add.html"
    fields=['name','year','description','image']
    success_url = reverse_lazy('home')
    # success_url=reverse_lazy('app:home')


# def edit(request,d):
#     b = movie.objects.get(id=d)
#     if (request.method == "POST"):
#         form = movieform(request.POST, request.FILES, instance=b)
#         if form.is_valid():
#             form.save()
#             return viewmovie(request,d=d)
#     form = movieform(instance=b)
#     return render(request,'edit.html',{'form':form})

class Update(UpdateView):
    model = movie
    template_name = "edit.html"
    fields = ['name', 'year', 'description', 'image']
    success_url = reverse_lazy('home')
    # success_url=reverse_lazy('app:home')

# def delete(request, d):
#     b = movie.objects.get(id=d)
#     b.delete()
#     return render(request,'home.html')

class Delete(DeleteView):
    model= movie
    template_name = "delete.html"
    success_url = reverse_lazy('home')
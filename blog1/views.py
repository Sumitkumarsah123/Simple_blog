from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm

from .models import Blog



# Create your views here.


# def home(request):
#      return render(request, 'blog.html')

def blog(request):
        
    data1=Blog.objects.all()
    return render(request, 'blog.html', {'data1':data1})
        

def create(request):
    if request.method=='POST':
        title= request.POST['title']
        writer= request.POST['writer']
        content= request.POST['content']
        data=Blog(title=title, writer=writer,content=content)
        data.save()
        print("data saved")
        return redirect('/')
    else:
        return render(request, 'blog_form.html')

class  BlogDetailView(DetailView):
     model= Blog
     template_name='blog_detail.html'
 


# dealing with generic view
class  BlogListView(ListView):
    model= Blog
    template_name='blog.html'
    context_object_name='data1'
    ordering= ['-date_posted']
    paginate_by=3

# @login_required()
# def blog_details(request, id):
#     detail= Blog.objects.get(id=id)
#     return render(request, 'blog_detail.html', {'detail':detail})

# dealing with generic views
class  BlogDetailView(DetailView):
     model= Blog
     template_name='blog_detail.html'
    

def edit(request, id):
    data1=Blog.objects.get(id=id)
    if request.method=='POST':
        data1.title= request.POST['title']
        # data1.writer= request.POST['writer']
        data1.content= request.POST['content']
        data1.save()
        return redirect ('/')
    else:
        return render(request, 'edit.html', {'data':data1})



 
def delete(request, id):
    data1=Blog.objects.get(id=id)
    data1.delete()
    return redirect('/')

def search(request):
    if request.method=='POST':
        search= request.POST['search']
        
        if search:
                data=Blog.objects.filter(Q(title__icontains=search))
                if data:
                    return render(request, 'search.html', {'sr':data})
                else:
                    messages.error(request, 'no result found')
                
                    return redirect('/')

        else:
            return HttpResponseRedirect("/search/")


    else:
        return render(request, 'search.html')


def feedback(request):
    if request.method=='POST':
        form= FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("data saved")
            return redirect('/')
        else:
            pass
    else:
        form= FeedbackForm()
    return render(request, "feedback.html", {'form':form})



           



    

from django.shortcuts import render,redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import book
from django.http import Http404

def home(request):
    allbooks = book.objects.all()
    context ={
        'allbooks' : allbooks
    }
    return render(request ,'yoshi/index.html' , context)
def detail(request , book_id):

    try:
        bk = book.objects.get(id = int(book_id))
    except book.DoesNotExist:
        raise Http404("Book Does Not exist!")

    return render(request , 'yoshi/details.html' , {'bk': bk})

def addbooks(request):
    if request.method == 'POST':
        bk = book.objects.create(
            name = request.POST.get('name'),
            author = request.POST.get('author'),
            type = request.POST.get('type'),
            price = request.POST.get('price')
        )

        bk.save()
        return redirect('home')
    return render(request , 'yoshi/addbook.html' , {})

def deletebook(request , pk):
    bk= book.objects.get(id=pk)
    if request.method == 'POST':
        bk.delete()
        return redirect('home')
    
    return render(request , 'yoshi/delete.html' , {'bk':bk})
    
    

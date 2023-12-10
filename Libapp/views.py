from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Book
# Create your views here.
def helloView(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})

def addBookView(request):
    return render(request,"addbook.html")


def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        a=request.POST["author"]
        g=request.POST["genre"]
        l=request.POST["language"]
        # p=request.POST["price"]
        print(t,a,g,l)
        book=Book()
        book.title=t
        book.author=a
        book.genre=g
        book.language=l
        # book.price=p
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        a=request.POST["author"]
        g=request.POST["genre"]
        l=request.POST["language"]
        # p=request.POST["price"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.author=a
        book.genre=g
        book.language=l
        # book.price=p
        book.save()
        return HttpResponseRedirect('/')


def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')

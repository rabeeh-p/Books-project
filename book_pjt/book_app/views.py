from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django. http import HttpResponse

# Create your views here.
@login_required(login_url='login')

def home(request):
    books_obj=Books.objects.all()
    section_obj=Category.objects.all()
    

    search=request.GET.get('search')
    category=request.GET.get('category')
    if search:
        books_obj= books_obj.filter(name__icontains=search)
    if category:
        books_obj= books_obj.filter(section_id=category)
         
    context={'book':books_obj,'category':section_obj}
    return render(request,'home.html',context)

def register(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser=User.objects.create_user(username=name,email=email,password=password)
        myuser.save()
        

    return render(request,'register.html')




def login(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        password=request.POST.get("password")
        new_user=auth.authenticate(username=name,password=password)

        if new_user:

            if new_user.is_staff:
                auth.login(request,new_user)
                return redirect('admin')
            else:
                auth.login(request,new_user)
                return redirect('home')
        else:
            return redirect('register')
        
        # elif(new_user):
        #     return redirect('home')
        
        # else:
        #     return redirect('register')
        # auth.login(request,new_user)
        # if new_user.is_staff==True:
            
        #     return redirect("sample")
        # elif new_user:
            
        #     auth.login(request,new_user)
        #     return redirect('home')
        
        
    return render(request,'login.html')


@login_required(login_url='login')
def admin(request):

    books_obj=Books.objects.all()

    context={'book':books_obj}

    return render(request,'admin.html',context)


@login_required(login_url='login')
def update_book(request,pk=None):
    book_n=Books.objects.get(id=pk)

    if  book_n.is_published == True:
        book_n.is_published = False
        book_n.save()
    else:
        book_n.is_published=True
        book_n.save()
    return redirect('admin')


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def create(request):
    
    if not request.user.is_superuser:
        return HttpResponse("invalid")

    section_obj=Category.objects.all()

    if request.method== 'POST':
        b_name= request.POST.get('name')
        b_author= request.POST.get('author')
        b_price= request.POST.get('price')
        
        category= request.POST.get('category')
        category_obj= Category.objects.get(id=category)
        
        
        image1=request.FILES['image']

        new=Books.objects.create(name=b_name,author=b_author,price=b_price,cover=image1,section=category_obj)
        new.save()
        return redirect('admin')
    

    return render(request,'create.html',{'cate':section_obj})



@login_required(login_url='login')
def view_page(request,id):

    book_obj=Books.objects.get(id=id)
    user=request.user
    if request.method=='POST':
        content=request.POST.get('content')
        Comment.objects.create(user=user,book=book_obj,content=content)


    commet_obj=Comment.objects.filter(book=book_obj)

    context={'book':book_obj,'comment':commet_obj}
    
    return render(request,'view.html',context)
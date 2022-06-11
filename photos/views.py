from django.shortcuts import render,redirect
from .models  import Category, Photo,Profile
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def  index(request):
        return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
               

                #log user in and redirect to settings page
               # user_login = auth.authenticate(username=username, password=password)
               # auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
 
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')     
 
def gallery (request):
       category = request.GET.get('category')
       if category == None:
            photos = Photo.objects.all()
       else:
           photos = Photo.objects.filter(category__name = category)
           
       category = Category.objects.all()
       context = {'categories':category,'photos':photos}
       return render(request,'gallery.html',context)
     
def viewPhoto (request, pk):
       photo = Photo.objects.get(id=pk)
       return render(request,'photo.html',{'photo':photo})
  
def addPhoto (request):
       category = Category.objects.all()
       if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                 
                name=data['category_new'])
        else:
            category = None
            
        photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )


        return redirect('gallery')

       context = {'categories': category}
       return render(request, 'add.html', context)
   
 

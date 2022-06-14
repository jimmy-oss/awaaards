import email
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models  import Category, Photo,Profile,Post,CategoryReview
from .form import ReviewAdd
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from itertools import chain

# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    userprofile = Profile.objects.get(user=user_object)

    return render(request, 'index.html', {'user_profile': userprofile})

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
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

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
       
       return render(request,'index.html',context)
     
 
 
def viewPhoto (request, pk):
       photo = Photo.objects.get(id=pk)
       reviewForm=ReviewAdd()
       return render(request,'photo.html',{'photo':photo,'form':reviewForm})
 
 

   
@login_required(login_url='signin')
def addPhoto (request):
       category = Category.objects.all()
       if request.method == 'POST':
        user = request.user.username
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
                 user=user,
                description=data['description'],
                image=image,
               submission_url=data['submission_url']
            )
         

        return redirect('gallery') 
       context = {'categories': category}
       return render(request, 'add.html', context)
   
 
  
@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            email_address = request.POST['email_address']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.email_address = email_address
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            email_address = request.POST['email_address']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.email_address = email_address
            user_profile.save()
        
        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})
     
@login_required(login_url='signin')
def profile(request, pk):
   
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Photo.objects.filter(user=pk)
    user_post_length = len(user_posts)

    
    user = pk  

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length
        
    }
    return render(request, 'profile.html', context)
@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})
  
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
   
 

from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Contact, Imagepost, Videopost,Userprofile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    return render(request , 'home.html')

def signup(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This username is already taken')
                return redirect("sign_up")
            elif User.objects.filter(email=email):
                messages.warning(request, 'This email is already taken , Please try other one!')
                return redirect("sign_up")

            else:
                user = User.objects.create_user(username=username ,password= password1 , email= email ,first_name=first_name , last_name = last_name)
                user.save()
                messages.success(request, 'Successfully Register! Now Please Login With Your Credentials') 
                return redirect("signin")
                    

        else:
            messages.warning(request, 'Password is not matching')  
            return redirect("sign_up")
                
    else:
        
        return render(request,'signup.html')

    
def signin(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password )

        if user is not None:
            auth.login(request , user)
            return redirect ("dashboard")

        else:
            
            messages.warning(request, 'Please Enter Valid Username & Password')  
            return redirect ("signin")
    else:
        return render(request,'signin.html')

def about(request):

    return render(request , 'about.html')

@login_required(login_url='signin')
def contact(request):

    if request.method == 'POST':
        name = request.POST.get('urname')
        mobile_no = request.POST.get('mobile_no')
        message = request.POST.get('message')

        usermessage = Contact(name = name , mobile_no = mobile_no, message = message)
        usermessage.save()
        messages.success(request, "The record has been saved successfully!")
        return redirect("/contact")

    return render(request , 'contact.html')
    
# def forget(request):

#     return render(request , 'forgetpassword.html')


def logout(request):

    auth.logout(request)
    return redirect("/")

@login_required(login_url='signin')
def dashboard(request):
    #fetchuserdata = Userprofile.objects.order_by('profilepic').last() #for getting last person or last data from database
    #fetchuserdata = Userprofile.objects.latest('profilepic') #for getting latest person or latest data from database
    fetchuserdata = Userprofile.objects.all().last() #for getting last person or last data from database
    fetchimagepost = Imagepost.objects.all()[::-1]
    fetchvideopost = Videopost.objects.all()[::-1]

    return render(request , 'dashboard.html', {'fetchimage':fetchimagepost , 'fetchvideo': fetchvideopost , 'fetchuser':fetchuserdata})

#Dashboard posts.........

def posts(request):

    if request.method == 'POST':
        if 'postimage' in request.POST:
        
            imgname = request.POST.get('imagename')
            photo = request.FILES['photo1']
            caption1 = request.POST.get('caption1')
            imagepostdata = Imagepost(image = photo, caption = caption1, imagename = imgname)
            imagepostdata.save()
            messages.success(request, "Image posted successfully!")
            return redirect("/dashboard")
        
        elif 'postvideo' in request.POST:
            vdoname = request.POST.get('videoname')
            utubelink = request.POST.get('utubelink')
            caption2 = request.POST.get('caption2')

            videopostdata = Videopost(utube_video_link  = utubelink, caption = caption2, videoname=vdoname)
            videopostdata.save()
            messages.success(request, "Video posted successfully!")
            return redirect("/dashboard")
        

       

    # elif request.method == 'POST':
    #     utubelink = request.POST.get('utubelink')
    #     caption2 = request.POST.get('caption2')
    #     videopostdata = Videopost(utube_video_link  = utubelink, caption = caption2)
    #     videopostdata.save()
    #     messages.success(request, "The video post has been saved successfully!")
    #     return redirect("/posts")

    
    return render(request , 'posts.html')

def editprofile(request):

    if request.method == 'POST':
        ppic = request.FILES['profilephoto']
        bio = request.POST.get('bio')
        userprofile = Userprofile(profilepic=ppic, about=bio)
        userprofile.save()
        messages.success(request, "Profile Updated!")

        return redirect('/dashboard')
        
    return render(request , 'editprofile.html')
        
def delete_post(request,post_id=None):
    post_to_delete=Imagepost.objects.get(id=post_id)
    post_to_delete.delete()
    messages.success(request, "Imagepost Deleted Successfully")
    
    return redirect('/dashboard')

def delete_postv(request,post_id=None):
    post_to_delete1=Videopost.objects.get(id=post_id)
    post_to_delete1.delete()
    messages.success(request, "Video post Deleted Successfully")
    
    return redirect('/dashboard')


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib.auth.models import *
from .models import *

import datetime
# Create your views here.

class UserAuth():
    
    def __init__(self,**kwargs):
        self.request = kwargs.get('request')
        
    def signUp(self):
        now = datetime.datetime.now()
        print (self.request)
        firstname = self.request.POST["firstname"]
        lastname = self.request.POST["lastname"]
        username = self.request.POST["username"]
        email = self.request.POST["email"]
        mobile = self.request.POST["mobile"]
        password = self.request.POST["password"]
        state = self.request.POST["state"]
        dob = datetime.datetime.strptime(self.request.POST["dob"],"%Y-%m-%d")
        gender = self.request.POST["gender"]
        state = self.request.POST["state"]
        address = self.request.POST["address"]
        blogObj = Blog.objects.filter(email=email,user__is_active=True)
        if not blogObj:

            user = User.objects.create_user(username=username,email=email,password=password)
            blog = Blog.objects.create(firstname=firstname,lastname=lastname,username=username,email=email,gender=gender,mobile=mobile,address=address,state=state,dob=dob)
    
            #send_mail("signup email","Succeful account creation","chopra.aayush24@gmail.com",[email],fail_silently=False,)
            return "User registered {0}\n <html><body><a href='/app1/authenticationpage/login/'>click here to login</a></body></html>".format(blog.email) 
        else:
            return "Already exist {0}".format(blogObj[0].email)

    def login(self):
        username = self.request.POST["username"]
        password = self.request.POST['password']
        print (username,password)
        blogObj = Blog.objects.filter(username=username)
        print (blogObj)
        checkUser = None
        if blogObj:
          try:
                checkUser = authenticate(username=username,password=password)
                login(self.request,checkUser)
                return "<html><body><a href='/app1/authenticationpage/logout/'>Click Here to Logout</a></body></html>"
          except:
                return "Incorrect username/password"
          if checkUser:  
                            
               return "Successfully Logged in"
        else: return "Incorrect User"
    def logout(self):
        pass

class Auth(View):


    def get(self,request,reqType):
        return render(request,"authentication_app1/"+reqType+".html")    
    
    def post(self,request,reqType):

        auth_user = UserAuth(request=request)
        
        if hasattr(auth_user,reqType):
            method = getattr(auth_user,reqType)
            res = method()
            print (res)
            return HttpResponse(res)
        else:
            return HttpResponse("Invalid request")
        
auth_request = csrf_exempt(Auth.as_view())

@csrf_exempt
def loginRequest(request):
    return render(request,"authentication_app1/login.html")




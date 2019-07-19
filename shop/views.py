from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
# from cart.cart import Cart
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

from pyrebase import pyrebase
from . models import *
from datetime import datetime

from django.conf import settings


import re
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User


from django.dispatch import receiver
from django.http import JsonResponse

import datetime
import time
from notify.signals import notify

import requests

import sys
import chilkat

config = {
    'apiKey': "AIzaSyAd8pc4st2fpBSt92GxeW9iF4Uql3j6LXI",
    'authDomain': "eduneer-82d2e.firebaseapp.com",
    'databaseURL':  "https://eduneer-82d2e.firebaseio.com",
    'projectId': "eduneer-82d2e",
    'storageBucket': "eduneer-82d2e.appspot.com",
    'messagingSenderId': "279848792993",
    'appId' : "1:279848792993:web:4d156db97784ae7b"
 
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()


# PPPPPPPPPPAAAAAAAAAAAAASSSSSSSSSSSSSWWWWWWWWWWWWWWWWWOOOOOOOOOOOOORRRRRRRRRRRRDDDDDDDDDDDDDDD
# eduneeradmin143



# email="admin@mujamall.com"
# passw = "admin123"

# auth.sign_in_with_email_and_password(email,passw)
# 

# user = firebase.auth().currentUser

# user = request.session.get('user')

def login(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"uk-active",
        'cart': cart
    }
    return render(request,"shop/login.html",context)


def landing(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"uk-active",
        'cart': cart

    }
    return render(request,"shop/normal/landing.html",context)


    

def register(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"uk-active",
        'cart': cart
    }
    return render(request,"shop/register.html",context)

def completeregister(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"uk-active",
        'cart': cart
    }
    return render(request,"shop/complete-register.html",context)

    

def forgot(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"uk-active",
        'cart': cart
    }
    return render(request,"shop/forgot_password.html",context)


def logout(request):
    # auth.current_user = None
    auth.logout(request)
    # request.user = None
    # request.session['user'] = None
    # request.session['checkout_redirect'] =  None
    # auth.signOut()
    return HttpResponseRedirect(reverse('shop:home')) 


def checkout(request):
    # The Chilkat API can be unlocked for a fully-functional 30-day trial by passing any
    # string to the UnlockBundle method.  A program can unlock once at the start. Once unlocked,
    # all subsequently instantiated objects are created in the unlocked state. 
    # 
    # After licensing Chilkat, replace the "Anything for 30-day trial" with the purchased unlock code.
    # To verify the purchased unlock code was recognized, examine the contents of the LastErrorText
    # property after unlocking.  For example:
    glob = chilkat.CkGlobal()
    success = glob.UnlockBundle("Anything for 30-day trial")
    if (success != True):
        print(glob.lastErrorText())
        sys.exit()

    status = glob.get_UnlockStatus()
    if (status == 2):
        print("Unlocked using purchased unlock code.")
    else:
        print("Unlocked in trial mode.")

    # The LastErrorText can be examined in the success case to see if it was unlocked in
    # trial more, or with a purchased unlock code.
    # print(glob.lastErrorText())



    rest = chilkat.CkRest()

    #  URL: https://www.paymestore.co/v2/buy/step2
    bTls = True
    port = 443
    bAutoReconnect = True
    success = rest.Connect("www.paymestore.co",port,bTls,bAutoReconnect)
    print(success)
    if (success != True):
        print("ConnectFailReason: " + str(rest.get_ConnectFailReason()))
        print(rest.lastErrorText())
        sys.exit()

    #  Note: The above code does not need to be repeatedly called for each REST request.
    #  The rest object can be setup once, and then many requests can be sent.  Chilkat will automatically
    #  reconnect within a FullRequest* method as needed.  It is only the very first connection that is explicitly
    #  made via the Connect method.

    rest.AddQueryParam("product_number","C66532")
    rest.AddQueryParam("data","{\"product_number\":\"C66532\"}")
    rest.AddQueryParam("_token","8ybVQkpjYH1xulohQ1VKFQ4rAeC3mkYZVqwSFsXy")

    rest.AddHeader("x-requested-with","XMLHttpRequest")
    rest.AddHeader("origin","https://www.paymestore.co")
    rest.AddHeader("accept-language","en-GB,en-US;q=0.9,en;q=0.8")
    rest.AddHeader("accept","*/*")
    rest.AddHeader("referer","https://www.paymestore.co/C66532")
    rest.AddHeader("accept-encoding","gzip, deflate, br")
    rest.AddHeader("authority","www.paymestore.co")

    strResponseBody = rest.fullRequestFormUrlEncoded("POST","/v2/buy/step2")
    print(rest.get_LastMethodSuccess())
    print(rest.get_ResponseStatusCode())
    if (rest.get_LastMethodSuccess() != True):
        print(rest.lastErrorText())
        sys.exit()

    respStatusCode = rest.get_ResponseStatusCode()
    if (respStatusCode >= 400):
        print("Response Status Code = " + str(respStatusCode))
        print("Response Header:")
        print(rest.responseHeader())
        print("Response Body:")
        print(strResponseBody)
        sys.exit()

    print("Response Body:")
    print(strResponseBody)
  
    # return HttpResponseRedirect(reverse('')) 
    return render(request,"shop/normal/landing.html")

def home(request):
    courses = db.child("courses").get()
    talks = db.child("talks").get()
    news = db.child("news").get()
    context = {
       
        "home_active":"uk-active",
        "courses":courses,
        "talks":talks,
        "news":news
        # 'cart': cart
    }
    return render(request,"shop/normal/landing.html",context)
    

def courses(request):
    # cart = Cart(request)
    courses = db.child("courses").get()
    
    context = {
       
        "courses_active":"uk-active",
         "courses":courses
    }
    # return render(request,"shop/courses.html",context)
    return render(request,"shop/normal/courses.html",context)
    

def mycourses(request):
    cart = Cart(request)

    
    context = {
       
        "my_courses_active":"uk-active",
        'cart': cart
    }
    return render(request,"shop/normal/mycourses.html",context)

def coursedetail(request,id):
    cart = Cart(request)
    course = db.child("courses").child(id).get()
    chapters = db.child("chapters").child(id).get()
    
    
    context = {
       
        "ajs":"uk-active",
        'cart': cart,
        "course":course,
        "chapters":chapters

    }
    # return render(request,"shop/course_detail.html",context)
    return render(request,"shop/normal/course_detail.html",context)


def newsdetail(request,id):
    cart = Cart(request)
    n = db.child("news").child(id).get()
    news = db.child("news").get()
    
    
    context = {
       
        "ajs":"uk-active",
        'cart': cart,
        "n":n,
        "news":news

    }
    # return render(request,"shop/course_detail.html",context)
    return render(request,"shop/normal/news_detail.html",context)


def coursedashboard(request,id1):
    # print(request.user)
    cart = Cart(request)

  
    chapters = db.child("chapters").child(id1).get()
    course = db.child("courses").child(id1).get()

    
    context = {
        "ajs":"uk-active",
        'cart': cart,
        "chapters":chapters,
        "course":course

    }
    return render(request,"shop/normal/course_dashboard.html",context)
  
      
        


def courselesson(request,id1,id2):
    # print(request.user)
    cart = Cart(request)

    chapter = db.child("chapters").child(id1).child(id2).get()
    lessons = db.child("chapters").child(id1).child(id2).child("lessons").get()
   
    course = db.child("courses").child(id1).get()

    
    context = {
       
        "ajs":"uk-active",
        'cart': cart,
        "chapter":chapter,
        "lessons":lessons,
        "course":course

    }
    return render(request,"shop/normal/course_lesson.html",context)

def talkdetail(request,id):
    talk = db.child("talks").child(id).get()
    cart = Cart(request)
  
    context = {    
        "ajs":"uk-active",
        'cart': cart,
        "talk":talk
    }
    return render(request,"shop/normal/talk_details.html",context)





def talks(request):
    talks = db.child("talks").get()
    cart = Cart(request)

    
    context = {
       
        "talks_active":"uk-active",
        'cart': cart,
        "talks":talks
    }
    return render(request,"shop/normal/talks.html",context)

def cart(request):
    cart = Cart(request)

    
    context = {
       
        "cart_active":"uk-active",
        'cart': cart
    }
    return render(request,"shop/cart.html",context)

def news(request):
    cart = Cart(request)
    news = db.child("news").get()
    
    context = {
       
        "news_active":"uk-active",
        'cart': cart,
        "news":news
    }
    return render(request,"shop/normal/news.html",context)

def contact(request):
    cart = Cart(request)

    
    context = {
       
        "contact_active":"uk-active",
        'cart': cart
    }
    return render(request,"shop/contact.html",context)


def partners(request):
    cart = Cart(request)

    
    context = {
       
        "partners_active":"uk-active",
        'cart': cart
    }
    return render(request,"shop/normal/partners.html",context)

def pay(request):
    cart = Cart(request)

    
    context = {
       
        "ski":"uk-active",
        'cart': cart
    }
    return render(request,"shop/pay.html",context)

def about(request):
    cart = Cart(request)

    
    context = {
       
        "about_active":"uk-active",
        'cart': cart
    }
    return render(request,"shop/normal/about.html",context)


    











































































































def dashboard(request):
    courses = db.child("courses").get()
    talks = db.child("talks").get()
    news = db.child("news").get()
    users_count = User.objects.all().count
    context = {
       
        "dashboard_active":"uk-active",
        "courses":courses,
        "talks":talks,
        "news":news,
        "users_count":users_count
       
    }
    return render(request,"shop/admin/home.html",context)


















def adminCategories(request):
    categories = db.child("categories").get()
    context = {
       
        "adminCourses_active":"uk-active",
        "categories":categories
       
    }
    return render(request,"shop/admin/categories.html",context)

    
def addcategory(request):
    data = {
        "name": request.POST.get('name'),
        "description": request.POST.get('description')
    }

    results = db.child("categories").push(data)
    
    messages.success(request, 'You have successfully added a course category 🖋')
    return HttpResponseRedirect(reverse('shop:adminCategories'))


def editcategory(request,id):
    old_name = request.POST.get('previous_name')
    courses = db.child("courses").get()
  
    data = {
        "name": request.POST.get('name'),
        "description": request.POST.get('description')
    }
    db.child("categories").child(id).update(data)
    
    aa = None
    if courses.each():
        for a in courses.each():
            aa = db.child("courses").order_by_child("category").equal_to(old_name).get()

    if aa:
        for b in aa.each():
            db.child("courses").child(b.key()).update(data2)  

    messages.info(request, 'You have successfully edited a course category 🖋')
    return HttpResponseRedirect(reverse('shop:adminCategories'))

def deletecategory(request,id):
    db.child("categories").child(id).remove()
    messages.error(request, 'You have deleted a course category 🗑')
    return HttpResponseRedirect(reverse('shop:adminCategories'))

def deletenews(request,id):
    db.child("news").child(id).remove()
    messages.error(request, 'You have deleted an article 🗑')
    return HttpResponseRedirect(reverse('shop:adminNews'))



def deletecourse(request,id):
    db.child("courses").child(id).remove()
    messages.error(request, 'You have deleted a course 🗑')
    return HttpResponseRedirect(reverse('shop:adminCourses'))


    
def deletechapter(request,courseid,chapterid):
    db.child("chapters").child(courseid).child(chapterid).remove()
    messages.success(request, 'You have successfully deleted the chapter 🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseChapter', kwargs={'id': courseid}))
 




def deletelesson(request,courseid,chapterid,id):
    db.child("chapters").child(courseid).child(chapterid).child("lessons").child(id).remove()
 
    messages.error(request, 'Lesosn Trashed  🗑')

    return HttpResponseRedirect(reverse('shop:adminCourseNewSubsection', kwargs={'id1': courseid,'id2': chapterid}))








def adminEarnings(request):
   
    context = {
       
        "adminEarnings_active":"uk-active",
       
    }
    return render(request,"shop/admin/earnings.html",context)

def adminStatements(request):
   
    context = {
       
        "adminStatements_active":"uk-active",
       
    }
    return render(request,"shop/admin/statements.html",context)

def adminAbout(request):
   
    context = {
       
        "adminWebinfo_active":"uk-active",
       
    }
    return render(request,"shop/admin/about.html",context)

def adminPartners(request):
   
    context = {
       
        "adminPartners_active":"uk-active",
       
    }
    return render(request,"shop/admin/partners.html",context)


def adminTalks(request):
    talks = db.child("talks").get()
    # talks = None
    context = {
       
        "adminTalks_active":"uk-active",
        "talks":talks
       
    }
    return render(request,"shop/admin/talks.html",context)


def adminNews(request):
    news = db.child("news").get()
    context = {
       
        "adminNews_active":"uk-active",
        "news":news
       
    }
    return render(request,"shop/admin/news.html",context)












def adminCourses(request):
    courses = db.child("courses").get()
    categories = db.child("categories").get()

    context = {
       
        "adminCourses_active":"uk-active",
        "courses":courses,
        "categories":categories
    }
    return render(request,"shop/admin/courses.html",context)





def addcourse(request):
    data = {
        "title": request.POST.get('title'),
        "sdescription": request.POST.get('sdescription'),
        "price": request.POST.get('price'),
        "fprice": request.POST.get('price'),
        "category": request.POST.get('category'),
        "ldescription": request.POST.get('ldescription'),
        "learn": request.POST.get('learn'),
        "requirements": request.POST.get('requirements'),
        "time_added":datetime.datetime.now().strftime("%c")
    }
# change this to category first
    results = db.child("courses").push(data)

    messages.success(request, 'You have successfully added a new course 🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseChapter', kwargs={'id': results['name']}))

def addchapter(request):
    data = {
        "title": request.POST.get('chapterTitle'),
        "time_added":datetime.datetime.now().strftime("%c"),
        "last_updated":datetime.datetime.now().strftime("%c")
    }
# change this to category first
    results = db.child("chapters").child(request.POST.get('id')).push(data)

    messages.success(request, 'You have successfully added a new course chapter🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseChapter', kwargs={'id': request.POST.get('id')}))



def addlesson(request):
    if request.FILES['fileUpload']:
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        storage = firebase.storage()
        # as user
        # user = request.session.get('user')
        
        thename = request.FILES['fileUpload']
        new_file = MyGenericModel(theFile=request.FILES['fileUpload'])      
        new_file.save()
        print(new_file.theFile.url)
        s = new_file.theFile.url + " "
        s = re.sub('/.*?/', '', s)
        # print(s)
        filer = re.sub('media', '', settings.MEDIA_ROOT)
        storage.child("files/"+s).put(filer + new_file.theFile.url)
        url = storage.child("files/"+s).get_url(request.user.id)



        # s = float(request.POST.get('duration'))
        # hours, remainder = divmod(s, 3600)
        # minutes, seconds = divmod(remainder, 60)
        # duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        duration = request.POST.get('duration')



        data = {
            "title": request.POST.get('lessonTitle'),
            "video_url":url,
            "duration": duration,
            "time_added":datetime.datetime.now().strftime("%c"),
            "last_updated":datetime.datetime.now().strftime("%c")
        }
    # change this to category first
        results = db.child("chapters").child(request.POST.get('courseid')).child(request.POST.get('chapterid')).child("lessons").push(data)

        messages.success(request, 'You have successfully added a new lesson to the course chapter🖋')
        user = User.objects.get(username="DextDerrickOmona")
    
  

        notify.send(request.user, recipient=user, actor=request.user, verb=request.POST.get('lessonTitle')+' was modified', nf_type='followed_by_one_user')
        return HttpResponseRedirect(reverse('shop:adminCourseNewSubsection', kwargs={'id1': request.POST.get('courseid'),'id2': request.POST.get('chapterid')}))

def edittalkvideo(request):
    if request.FILES['fileUpload']:
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        storage = firebase.storage()
        # as user
        # user = request.session.get('user')
        
        thename = request.FILES['fileUpload']
        new_file = MyGenericModel(theFile=request.FILES['fileUpload'])      
        new_file.save()
        print(new_file.theFile.url)
        s = new_file.theFile.url + " "
        s = re.sub('/.*?/', '', s)
        # print(s)
        filer = re.sub('media', '', settings.MEDIA_ROOT)
        storage.child("files/"+s).put(filer + new_file.theFile.url)
        url = storage.child("files/"+s).get_url(request.user.id)



        # s = float(request.POST.get('duration'))
        # hours, remainder = divmod(s, 3600)
        # minutes, seconds = divmod(remainder, 60)
        # duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        duration = request.POST.get('duration')



        data = {
          
            "video_url":url,
            "duration": duration,
            "last_updated":datetime.datetime.now().strftime("%c")
        }
    # change this to category first
        results = db.child("talks").child(request.POST.get('talkid')).update(data)

        messages.success(request, 'You have successfully added a video for the talk🖋')
        return HttpResponseRedirect(reverse('shop:adminTalkNewContent', kwargs={'id': request.POST.get('talkid')}))



def editlesson(request):

    data = {
        "title": request.POST.get('lessonTitle2'),
 
        "last_updated":datetime.datetime.now().strftime("%c")
    }

    results = db.child("chapters").child(request.POST.get('courseid')).child(request.POST.get('chapterid')).child("lessons").child(request.POST.get('lessonid')).update(data)

    messages.success(request, 'Changes were successfully made on the lesson 🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseNewSubsection', kwargs={'id1': request.POST.get('courseid'),'id2': request.POST.get('chapterid')}))
    


   

def editchapter(request):
    data = {
        "title": request.POST.get('chapterTitle'),
        # "chapterNumber":  request.POST.get('chapterNumber'),
        "last_updated":datetime.datetime.now().strftime("%c")
    }
    # change this to category first
    results = db.child("chapters").child(request.POST.get('courseid')).child(request.POST.get('chapterid')).update(data)

    messages.success(request, 'You have successfully edited the chapter 🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseNewSubsection', kwargs={'id1': request.POST.get('courseid'),'id2': request.POST.get('chapterid')}))
 




def editcourse(request): 
    data = {
        "title": request.POST.get('title'),
        "sdescription": request.POST.get('sdescription'),
        "price": request.POST.get('price'),
        "fprice": request.POST.get('price'),
        "category": request.POST.get('category'),
        "ldescription": request.POST.get('ldescription'),
        "learn": request.POST.get('learn'),
        "requirements": request.POST.get('requirements'),
        "last_updated":datetime.datetime.now().strftime("%c")
    }
    db.child("courses").child(request.POST.get('courseid')).update(data)
  
    messages.info(request, 'You have successfully edited a course 🖋')
    return HttpResponseRedirect(reverse('shop:adminCourses'))

def editcover(request): 
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    # user = request.session.get('user')
    thename = request.FILES['cover']
    new_file = MyGenericModel(theFile=request.FILES['cover'])      
    new_file.save()
    print(new_file.theFile.url)
    s = new_file.theFile.url + " "
    s = re.sub('/.*?/', '', s)
    # print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("covers/"+s).put(filer + new_file.theFile.url)
    url = storage.child("covers/"+s).get_url(request.user.id)

    data = {
        "cover": url
    }
# change this to category first
    results = db.child("courses").child(request.POST.get('courseid')).update(data)

    messages.success(request, 'You have changed the cover photo for this course🖋')
    return HttpResponseRedirect(reverse('shop:adminCourseChapter', kwargs={'id': request.POST.get('courseid')}))


def edittalkcover(request): 
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    # user = request.session.get('user')
    thename = request.FILES['cover']
    new_file = MyGenericModel(theFile=request.FILES['cover'])      
    new_file.save()
    print(new_file.theFile.url)
    s = new_file.theFile.url + " "
    s = re.sub('/.*?/', '', s)
    # print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("covers/"+s).put(filer + new_file.theFile.url)
    url = storage.child("covers/"+s).get_url(request.user.id)

    data = {
        "cover": url
    }
# change this to category first
    results = db.child("talks").child(request.POST.get('talkid')).update(data)

    messages.success(request, 'You have changed the cover photo for this talk')
    return HttpResponseRedirect(reverse('shop:adminTalkNewContent', kwargs={'id': request.POST.get('talkid')}))
    




def adminCourseNew(request):
    categories = db.child("categories").get()
    context = {
       
        "adminCourses_active":"uk-active",
           "categories":categories
    }
    return render(request,"shop/admin/new-course.html",context)



def adminCourseChapter(request,id):
    course = db.child("courses").child(id).get()
    chapters = db.child("chapters").child(id).get()
    categories = db.child("categories").get()

    context = {
       
        "adminCourses_active":"uk-active",
        "course":course,
        "chapters":chapters,
        "categories":categories
    }
  
    return render(request,"shop/admin/course-chapter.html",context)

def adminNewsDetail(request,id):
    a = db.child("news").child(id).get()


    context = {
       
        "adminNews_active":"uk-active",
        "a":a
    }
  
    return render(request,"shop/admin/news_detail.html",context)

def adminCourseNewSubsection(request,id1,id2):

    chapter = db.child("chapters").child(id1).child(id2).get()
    lessons = db.child("chapters").child(id1).child(id2).child("lessons").get()
    course = db.child("courses").child(id1).get()

    # if lessons.each():
    #     sss = 0
    #     for a in lessons.each():
    #         print(a)
    #         sss += time.strptime(a.val().duration,'%H:%M:%S')
    #         print(sss)
       

    context = {
       
        "adminCourses_active":"uk-active",
        "chapter":chapter,
        "course":course,
        "lessons":lessons
       
    }
    return render(request,"shop/admin/course-content.html",context)


    


    

def adminCourseEdit(request):
    course = db.child("courses").child(id).get()
    chapters = db.child("chapters").child(id).get()
    context = {
       
        "adminCourses_active":"uk-active",
        "course":course,
        "chapters":chapters
    }
    return render(request,"shop/admin/edit-course.html",context)


def adminTalkNew(request):
   
    context = {
       
        "adminTalks_active":"uk-active",
       
    }
    return render(request,"shop/admin/new-talk.html",context)


def addtalk(request):
    data = {
        "title": request.POST.get('title'),
        "sdescription": request.POST.get('sdescription'),
        "about": request.POST.get('about'),
        "creator_name": request.POST.get('creator_name'),
        "creator_about": request.POST.get('creator_about'),
        "time_added":datetime.datetime.now().strftime("%c")
    }
# change this to category first
    results = db.child("talks").push(data)

    messages.success(request, 'You have successfully added a new talk 🖋')
    return HttpResponseRedirect(reverse('shop:adminTalks'))


def addnews(request):
    data = {
        "title": request.POST.get('title'),
        "sdescription": request.POST.get('sdescription'),
        "article": request.POST.get('article'),
        "about": request.POST.get('about'),
        "written_by": request.POST.get('written_by'),

        "time_added":datetime.datetime.now().strftime("%c")
    }
# change this to category first
    results = db.child("news").push(data)

    messages.success(request, 'You have successfully added a new article 🖋')
    return HttpResponseRedirect(reverse('shop:adminNews'))





def editnews(request):

    data = {
        "title": request.POST.get('title'),
        "sdescription": request.POST.get('sdescription'),
        "article": request.POST.get('article'),
        "about": request.POST.get('about'),
        "written_by": request.POST.get('written_by'),
 
        "last_updated":datetime.datetime.now().strftime("%c")
    }


    results = db.child("news").child(request.POST.get('newsid')).update(data)

    messages.success(request, 'Changes were successfully made on the article 🖋')
    return HttpResponseRedirect(reverse('shop:adminNewsDetail', kwargs={'id': request.POST.get('newsid')}))
   
    




def adminTalkNewContent(request,id):
   

    talk = db.child("talks").child(id).get()
  

    context = {
       
        "adminTalks_active":"uk-active",
        "talk":talk
    }
  
    return render(request,"shop/admin/talk-content.html",context)

def adminTalkEdit(request):
   
    context = {
       
        "adminTalks_active":"uk-active",
       
    }
    return render(request,"shop/admin/edit-talk.html",context)



    

    

    

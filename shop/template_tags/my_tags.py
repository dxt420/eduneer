from django import template
from pyrebase import pyrebase
from num2words import num2words

from datetime import datetime
from django.contrib.auth.models import User

from social_django.models import UserSocialAuth

register = template.Library()

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
db = firebase.database()

@register.simple_tag
def numberToWord(a):
    return num2words(a)
     
     

@register.simple_tag
def timer(sss):
    s = float(sss)
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    return duration

@register.simple_tag
def getLessonTitle(courseID,chapterID,lessonID):
    lesson = db.child("chapters").child(courseID).child(chapterID).child("lessons").child(lessonID).get()
    return lesson.val()["title"]

@register.simple_tag
def getLessonVideoUrl(courseID,chapterID,lessonID):
    lesson = db.child("chapters").child(courseID).child(chapterID).child("lessons").child(lessonID).get()
    return lesson.val()["video_url"]

@register.simple_tag
def getLessonDuration(courseID,chapterID,lessonID):
    lesson = db.child("chapters").child(courseID).child(chapterID).child("lessons").child(lessonID).get()
    s = float(lesson.val()["duration"])
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    return duration
   


@register.simple_tag
def readableTime(strr):
    datetime_object = datetime.strptime(strr, '%c')
    return datetime_object.strftime("%A %B %d %Y  at %I:%M %p")


@register.simple_tag
def getAvatar(username):
    user = UserSocialAuth.objects.get(user=username)
  
    if user.provider == "google-oauth2":
        return user.extra_data["picture"]
    elif user.provider == "facebook":
        return user.extra_data["picture"].data.url
    




from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    path('landing', views.landing , name="landing"),
    
    path('', views.home , name="home"),
    path('courses', views.courses , name="courses"),
    path('mycourses', views.mycourses , name="mycourses"),
    path('coursedetail/<slug:id>', views.coursedetail , name="coursedetail"),
path('coursedashboard/<slug:id1>', views.coursedashboard , name="coursedashboard"),
path('courselesson/<slug:id1>/<slug:id2>', views.courselesson , name="courselesson"),




path('newsdetail/<slug:id>', views.newsdetail , name="newsdetail"),
    
    path('talks', views.talks , name="talks"),
    path('talkdetail/<slug:id>', views.talkdetail , name="talkdetail"),
    path('cart', views.cart , name="cart"),
    path('news', views.news , name="news"),
    path('contact', views.contact , name="contact"),
    path('partners', views.partners , name="partners"),
    path('pay', views.pay , name="pay"),
    path('about', views.about , name="about"),
    path('register', views.register , name="register"),
    path('completeregister', views.completeregister , name="completeregister"),
    path('login', views.login , name="login"),
    path('logout', views.logout , name="logout"),
    path('forgot', views.forgot , name="forgot"),


    path('dashboard', views.dashboard , name="dashboard"),


    path('manage-courses', views.adminCourses , name="adminCourses"),
    path('manage-categories', views.adminCategories , name="adminCategories"),
    path('addcategory', views.addcategory , name="addcategory"),
     path('deletecategory/<slug:id>', views.deletecategory , name="deletecategory"),
     path('deletenews/<slug:id>', views.deletenews , name="deletenews"),
      path('deletecourse/<slug:id>', views.deletecourse , name="deletecourse"),
      path('deletechapter/<slug:courseid>/<slug:chapterid>', views.deletechapter , name="deletechapter"),
      path('editcategory/<slug:id>', views.editcategory , name="editcategory"),


      path('editcategory/<slug:id>', views.editcategory , name="editcategory"),



      

    path('editcourse', views.editcourse , name="editcourse"),
    
    path('earnings', views.adminEarnings , name="adminEarnings"),
    path('statements', views.adminStatements , name="adminStatements"),
    path('manage-about', views.adminAbout , name="adminAbout"),
    path('manage-partners', views.adminPartners , name="adminPartners"),
    path('manage-talks', views.adminTalks , name="adminTalks"),
    path('addtalk', views.addtalk , name="addtalk"),

    path('manage-news', views.adminNews , name="adminNews"),



    path('new-course', views.adminCourseNew , name="adminCourseNew"),
    path('course-chapter/<slug:id>', views.adminCourseChapter , name="adminCourseChapter"),
     path('news-detail-edit/<slug:id>', views.adminNewsDetail , name="adminNewsDetail"),

    
    path('course-chapter-sub-section/<slug:id1>/<slug:id2>', views.adminCourseNewSubsection , name="adminCourseNewSubsection"),
    path('edit-course/<slug:id>', views.editcategory , name="editcategory"),
    path('addcourse', views.addcourse , name="addcourse"),
     path('addchapter', views.addchapter , name="addchapter"),
     path('editchapter', views.editchapter , name="editchapter"),

          path('addlesson', views.addlesson , name="addlesson"),
            path('editlesson', views.editlesson , name="editlesson"),
            path('deletelesson/<slug:courseid>/<slug:chapterid>/<slug:id>', views.deletelesson , name="deletelesson"),
              path('editcover', views.editcover , name="editcover"),
                  path('edittalkcover', views.edittalkcover , name="edittalkcover"),

                   path('addnews', views.addnews , name="addnews"),



              

            

       path('edittalkvideo', views.edittalkvideo , name="edittalkvideo"),

   

    path('new-talk', views.adminTalkNew , name="adminTalkNew"),
     path('talk-content/<slug:id>', views.adminTalkNewContent , name="adminTalkNewContent"),
     path('edit-talk', views.adminTalkEdit , name="adminTalkEdit"),
    
    
]

 
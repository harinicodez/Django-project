# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),  
#     path('login/', views.login, name='login'), 
#     path('blog/',views.myblog,name='blogdata'),
#     path('signdata/blog/',views.signupdata,name='signupdata'),
#     path('signdata/blog/signup/',views.signup,name='signuplog'),
#     path('signdata/blog/login/',views.login,name='tologin'),
#     path('blog/<int:blogid>/',views.myblogid,name='loadpage'),
#     path('blog/signup/',views.signup),
#     path('blog/login/',views.signup),
#     path('login/security/',views.authenticationForLogin,name='authenticate')

  

# ]

from django.urls import path
from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),  
    path('login/', views.login, name='login'), 
    path('login/security/blog/auth/signup/', views.signup, name='login'),
    path('blog/signup/', views.myblog, name='blogdata'),
    path('blog/login/', views.myblog, name='blogdata'),
    path('blog/',views.myblog),
    path('blog/<int:blogid>/', views.myblogid, name='loadpage'),
    path('signup/security/blog/', views.signupdata, name='signupdata'),
    path('login/security/blog/', views.authenticationForLogin, name='authenticate'),
    path('blog/signup/',views.signup),
    path('blog/login',views.login),
    path('signdata/blog/login/',views.login),
    path('signdata/blog/signup/',views.signupdata),
    path('home/',views.home,name = 'homepage'),
    path('signup/security/blog/home/',views.home),
    path('signup/auth/login/',views.login,name='log'),
    path('signup/auth/login/security/blog/',views.authenticationForLogin),


    
]

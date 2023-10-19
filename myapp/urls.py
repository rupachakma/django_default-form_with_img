from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="homepage"),
    path('signuppage', views.signuppage,name="signuppage"),
    path('loginpage', views.loginpage,name="loginpage"),
    path('addpage', views.addpage,name="addpage"),
    path('updatepage/<int:id>', views.updatepage,name="updatepage"),
    path('deletepage/<int:id>',views.deletepage,name="deletepage"),
    path('dashboardpage', views.dashboardpage,name="dashboardpage"),
    path('aboutpage', views.aboutpage,name="aboutpage"),
    path('logoutpage', views.logoutpage,name="logoutpage"),
]
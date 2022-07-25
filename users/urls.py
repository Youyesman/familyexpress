from django.urls import path
from .views import * # user>views에서 모든 함수를 가져온다.
from django.contrib.auth import views as auth_views
import users.views

app_name = "users"
urlpatterns = [
     path('login/', users.views.login, name='login'),
     path('logout/', users.views.logout, name='logout'),
     path('signup/', users.views.signup, name='signup'),

]
from django.shortcuts import render, redirect

from .forms import Userform
from .models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth


# Create your views here.

# 회원 가입


def signup(request):

    if request.user.is_authenticated:
        # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
        return redirect('/feg')
    else:
        if request.method == 'POST':
            # password와 confirm에 입력된 값이 같다면
            form = Userform(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['confirm']:

                    # user 객체를 새로 생성
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'], 
                        password=form.cleaned_data['password'],
                        )
                    user.team = form.cleaned_data['team']
                    user.name = form.cleaned_data['name']
                    user.email = form.cleaned_data['email']  
                    user.save()
                    # 로그인 한다
                    
                    auth.login(request, user)

                    return redirect('/users/login')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
        return render(request, 'users/signup.html')


def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/feg')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'users/recheck.html')
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'users/login.html')

# 로그 아웃


def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'GET':
        auth_logout(request)
        return redirect('/users/login')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'users/login.html')


def change_password(request):
  if request.method == "POST":
    user = request.user
    origin_password = request.POST["origin_password"]
    if check_password(origin_password, user.password):
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/users/login')
      else:
        messages.error(request, 'Password not same')
    else:
      messages.error(request, 'Password not correct')
    return render(request, 'users/change_password.html')
  else:
    return render(request, 'users/change_password.html')
from collections import UserList
from django.shortcuts import render, redirect

from users.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from familyexpress.decorators import *
from users import *
from django.core.paginator import Paginator
from . import models

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def posting(request,id):
    post = Post.objects.get(pk=id)
    return render(request, "feg/posting.html", {'post':post})

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def post_list(request):
    page = request.GET.get("page")
    posts_list = models.Post.objects.get_queryset().order_by('-id')
    paginator = Paginator(posts_list,10)
    posts = paginator.get_page(page)
    context = {'post_list': Post.objects.all(),'page':posts}
    return render(request, "feg/post_list.html", context)

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def post_form(request, id=0):
    post = Post.objects.get(pk=id)

    if request.method == "GET":
        if id == 0:
            form = PostForm()
        elif post.username.id == request.user.pk:
            post = Post.objects.get(pk=id)            
            form = PostForm(instance=post)
            return render(request, "feg/post_form.html", {'form': form})
        else:
           return redirect('/feg/404.html')
    else:
        if id == 0:
            form = PostForm(request.POST)
        elif post.username.id == request.user.pk:
            post = Post.objects.get(pk=id)     
            form = PostForm(request.POST, instance=post)
        else:
           return redirect('/feg/404.html')    
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/post_list.html')

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')    
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    if post.username.id == request.user.pk:
        post.delete()
        return redirect('/feg/post_list.html')
    else:
        return redirect('/feg/404.html') 
    

###########################################################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def FCL_list(request):
    context = {'fcl_list': FCL.objects.all()}
    return render(request, "feg/FCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def FCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = FCLForm()
        else:
            fcl = FCL.objects.get(pk=id)
            form = FCLForm(instance=fcl)
        return render(request, "feg/FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = FCLForm(request.POST)
        else:
            fcl = FCL.objects.get(pk=id)
            form = FCLForm(request.POST, instance=fcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/FCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def FCL_delete(request, id):
    fcl = FCL.objects.get(pk=id)
    fcl.delete()
    return redirect('/feg/FCL_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def AIR_list(request):
    context = {'airfreight_list': Airfreight.objects.all()}
    return render(request, "feg/AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = AirfreightForm()
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(instance=airfreight)
        return render(request, "feg/AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = AirfreightForm(request.POST)
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(request.POST, instance=airfreight)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def AIR_delete(request, id):
    airfreight = Airfreight.objects.get(pk=id)
    airfreight.delete()
    return redirect('/feg/AIR_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def LCL_list(request):
    context = {'lcl_list': LCL.objects.all()}
    return render(request, "feg/LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def LCL_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = LCLForm()
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(instance=lcl)
        return render(request, "feg/LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = LCLForm(request.POST)
            
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(request.POST, instance=lcl)
            
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            # form.LCL_origin = request.POST.get('origin')
            # form.LCL_chk_date = request.POST.get('chk_date')
            # form.LCL_dest = request.POST.get('destination')
            # form.LCL_ofc = request.POST.get('ofc')
            # form.ofcunit = request.POST.get('ofcunit')
            # form.LCL_ttime = request.POST.get('ttime')
            # form.LCL_remark = request.POST.get('remark')
            # form.LCL_effective = request.POST.get('effective')
            # form.LCL_consol = request.POST.get('consol')
            form.save()
            
            
            
        return redirect('/feg/LCL_list.html')
    

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def LCL_delete(request, id):
    lcl = LCL.objects.get(pk=id)
    lcl.delete()
    return redirect('/feg/LCL_list.html')

#############################################################################################


def error(request):
    return render(request, 'feg/404.html')

def forgotpassword(request):
    return render(request, 'feg/forgot-password.html')


def index(request):
    page = request.GET.get("page")
    posts_list = models.Post.objects.get_queryset().order_by('-id')
    paginator = Paginator(posts_list,5)
    posts = paginator.get_page(page)
    context = {'post_list': Post.objects.all(),'page':posts}
    return render(request, 'feg/index.html', context)


def register(request):
    return render(request, 'feg/register.html')


def search(request):
    qs = FCL.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(dest__icontains=q) | qs.filter(origin__icontains=q) | qs.filter(
            carrier__icontains=q) 

    return render(request, 'feg/search.html', {
        'fcl_list': qs,
        'q': q,

    })


def searchair(request):
    qs = Airfreight.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(air_consol__icontains=q) | qs.filter(air_origin__icontains=q)\
            | qs.filter(air_dest__icontains=q)

    return render(request, 'feg/searchair.html', {
        'airfreight_list': qs,
        'q': q,

    })


def searchlcl(request):
    qs = LCL.objects.all()
    q = request.GET.get('q', '')  # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(LCL_origin__icontains=q) | qs.filter(LCL_dest__icontains=q)\
            | qs.filter(LCL_consol__icontains=q) 

    return render(request, 'feg/searchlcl.html', {
        'lcl_list': qs,
        'q': q,

    })

    ###################################################################################################################################

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_Air_list(request):
    context = {'Local_airfreight_list': Local_Air.objects.all()}
    return render(request, "feg/Local_AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Local_AirForm()
            
        else:
            localairfreight = Local_Air.objects.get(pk=id)
            form = Local_AirForm(instance=localairfreight)
        return render(request, "feg/Local_AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = Local_AirForm(request.POST)
        else:
            localairfreight = Local_Air.objects.get(pk=id)
            form = Local_AirForm(request.POST, instance=localairfreight)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Local_AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_AIR_delete(request, id):
    localairfreight = Local_Air.objects.get(pk=id)
    localairfreight.delete()
    return redirect('/feg/Local_AIR_list.html')

##############################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_LCL_list(request):
    context = {'Local_lcl_list': Local_Lcl.objects.all()}
    return render(request, "feg/Local_LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_LCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Local_LclForm()
            
        else:
            locallcl = Local_Lcl.objects.get(pk=id)
            form = Local_LclForm(instance=locallcl)
        return render(request, "feg/Local_LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = Local_LclForm(request.POST)
        else:
            locallcl = Local_Lcl.objects.get(pk=id)
            form = Local_LclForm(request.POST, instance=locallcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Local_LCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_LCL_delete(request, id):
    locallcl = Local_Fcl.objects.get(pk=id)
    locallcl.delete()
    return redirect('/feg/Local_LCL_list.html')


##############################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_FCL_list(request):
    context = {'Local_Fcl_list': Local_Fcl.objects.all()}
    return render(request, "feg/Local_FCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_FCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Local_FclForm()
            
        else:
            localfcl = Local_Fcl.objects.get(pk=id)
            form = Local_FclForm(instance=localfcl)
        return render(request, "feg/Local_FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = Local_FclForm(request.POST)
        else:
            localfcl = Local_Fcl.objects.get(pk=id)
            form = Local_FclForm(request.POST, instance=localfcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Local_FCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Local_FCL_delete(request, id):
    localfcl = Local_Fcl.objects.get(pk=id)
    localfcl.delete()
    return redirect('/feg/Local_FCL_list.html')

###########################################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_FCL_list(request):
    context = {'Dest_Fcl_list': Dest_Fcl.objects.all()}
    return render(request, "feg/Dest_FCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_FCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Dest_FclForm()
            
        else:
            destfcl = Dest_Fcl.objects.get(pk=id)
            form = Dest_FclForm(instance=destfcl)
        return render(request, "feg/Dest_FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = Dest_FclForm(request.POST)
        else:
            destfcl = Dest_Fcl.objects.get(pk=id)
            form = Dest_FclForm(request.POST, instance=destfcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Dest_FCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_FCL_delete(request, id):
    destfcl = Dest_Fcl.objects.get(pk=id)
    destfcl.delete()
    return redirect('/feg/Dest_FCL_list.html')

######################################################################################

@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_LCL_list(request):
    context = {'Dest_Lcl_list': Dest_Lcl.objects.all()}
    return render(request, "feg/Dest_LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_LCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Dest_LclForm()
            
        else:
            destlcl = Dest_Lcl.objects.get(pk=id)
            form = Dest_LclForm(instance=destlcl)
        return render(request, "feg/Dest_LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = Dest_LclForm(request.POST)
        else:
            destlcl = Dest_Lcl.objects.get(pk=id)
            form = Dest_LclForm(request.POST, instance=destlcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Dest_LCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_LCL_delete(request, id):
    destlcl = Dest_Lcl.objects.get(pk=id)
    destlcl.delete()
    return redirect('/feg/Dest_LCL_list.html')

##########################################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_AIR_list(request):
    context = {'Dest_Air_list': Dest_Air.objects.all()}
    return render(request, "feg/Dest_AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Dest_AirForm()
            
        else:
            destair = Dest_Air.objects.get(pk=id)
            form = Dest_AirForm(instance=destair)
        return render(request, "feg/Dest_AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = Dest_AirForm(request.POST)
        else:
            destair = Dest_Air.objects.get(pk=id)
            form = Dest_AirForm(request.POST, instance=destair)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/feg/Dest_AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/feg/404.html')
def Dest_AIR_delete(request, id):
    destair = Dest_Air.objects.get(pk=id)
    destair.delete()
    return redirect('/feg/Dest_AIR_list.html')
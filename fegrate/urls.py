from django.urls import path,include
from . import views
from fegrate.views import *

urlpatterns = [
    path('feg/',views.index,name='index'),
    path('feg/post',views.post_form,name='post_insert'),
    path('feg/post/<int:id>',views.post_form,name='post_update'),
    path('feg/post/delete/<int:id>',views.post_delete,name= 'post_delete'),
    path('feg/post_list.html',views.post_list,name= 'post_list'),
    path('feg/posting/<int:id>',views.posting,name= 'posting'),
    
    path('feg/FCL/', views.FCL_form,name='FCL_insert'), # get and post req. for insert operation
    path('feg/FCL/<int:id>/', views.FCL_form,name='FCL_update'), # get and post req. for update operation
    path('feg/FCL/delete/<int:id>/',views.FCL_delete,name='FCL_delete'),
    path('feg/FCL_list.html',views.FCL_list,name='FCL_list'),
    
    path('feg/LCL/', views.LCL_form,name='LCL_insert'), # get and post req. for insert operation
    path('feg/LCL/<int:id>/', views.LCL_form,name='LCL_update'), # get and post req. for update operation
    path('feg/LCL/delete/<int:id>/',views.LCL_delete,name='LCL_delete'),
    path('feg/LCL_list.html',views.LCL_list,name='LCL_list'),# get req. to retrieve and display all records
    path('feg/AIR/', views.AIR_form, name='AIR_insert'),
    path('feg/AIR/<int:id>/', views.AIR_form,name='AIR_update'), # get and post req. for update operation
    path('feg/AIR/delete/<int:id>/',views.AIR_delete,name='AIR_delete'),
    path('feg/AIR_list.html/',views.AIR_list,name='AIR_list'),
    path('feg/404.html', views.error, name='error'),
    path('feg/forgot-password.html', views.forgotpassword, name='forgotpassword'),
    path('feg/index.html', views.index, name='index'),
    path('feg/register.html', views.register, name='register'),
    path('feg/search/',views.search, name="search"),
    path('feg/searchair/',views.searchair, name="searchair"),
    path('feg/searchlcl/',views.searchlcl, name="searchlcl"),
    path('feg/Local_AIR/', views.Local_AIR_form, name='Local_AIR_insert'),
    path('feg/Local_AIR/<int:id>/', views.Local_AIR_form,name='Local_AIR_update'), # get and post req. for update operation
    path('feg/Local_AIR/delete/<int:id>/',views.Local_AIR_delete,name='Local_AIR_delete'),
    path('feg/Local_AIR_list.html/',views.Local_Air_list,name='Local_AIR_list'),
    path('feg/Local_LCL/', views.Local_LCL_form, name='Local_LCL_insert'),
    path('feg/Local_LCL/<int:id>/', views.Local_LCL_form,name='Local_LCL_update'), # get and post req. for update operation
    path('feg/Local_LCL/delete/<int:id>/',views.Local_LCL_delete,name='Local_LCL_delete'),
    path('feg/Local_LCL_list.html/',views.Local_LCL_list,name='Local_LCL_list'),
    path('feg/Local_FCL/', views.Local_FCL_form, name='Local_FCL_insert'),
    path('feg/Local_FCL/<int:id>/', views.Local_FCL_form,name='Local_FCL_update'), # get and post req. for update operation
    path('feg/Local_FCL/delete/<int:id>/',views.Local_FCL_delete,name='Local_FCL_delete'),
    path('feg/Local_FCL_list.html/',views.Local_FCL_list,name='Local_FCL_list'),
    path('feg/Dest_AIR/', views.Dest_AIR_form, name='Dest_AIR_insert'),
    path('feg/Dest_AIR/<int:id>/', views.Dest_AIR_form,name='Dest_AIR_update'), # get and post req. for update operation
    path('feg/Dest_AIR/delete/<int:id>/',views.Dest_AIR_delete,name='Dest_AIR_delete'),
    path('feg/Dest_AIR_list.html/',views.Dest_AIR_list,name='Dest_AIR_list'),
    path('feg/Dest_LCL/', views.Dest_LCL_form, name='Dest_LCL_insert'),
    path('feg/Dest_LCL/<int:id>/', views.Dest_LCL_form,name='Dest_LCL_update'), # get and post req. for update operation
    path('feg/Dest_LCL/delete/<int:id>/',views.Dest_LCL_delete,name='Dest_LCL_delete'),
    path('feg/Dest_LCL_list.html/',views.Dest_LCL_list,name='Dest_LCL_list'),
    path('feg/Dest_FCL/', views.Dest_FCL_form, name='Dest_FCL_insert'),
    path('feg/Dest_FCL/<int:id>/', views.Dest_FCL_form,name='Dest_FCL_update'), # get and post req. for update operation
    path('feg/Dest_FCL/delete/<int:id>/',views.Dest_FCL_delete,name='Dest_FCL_delete'),
    path('feg/Dest_FCL_list.html/',views.Dest_FCL_list,name='Dest_FCL_list'),
]

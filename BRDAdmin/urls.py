from django.urls import path
from . import views

urlpatterns=[

    path('login/',views.fnlogin,name="login"),
    path('logout/',views.fnlogout,name="logout"),

    path('home/',views.fnhome,name="home"),

    path('roles/',views.fnroles,name="roles"),
    path('add_roles/',views.fnadd_roles,name="add_roles"),
    path('disable_roles/<roledis_id>',views.fndisable_roles,name="disable_roles"),
    path('edit_role/<editrole_id>',views.fnedit_roles,name="edit_role"),
    path('add_permissions/<perm_id>',views.fnadd_permissions,name="add_permissions"),

    path('users/',views.fnusers,name="users"),
    path('add_user/',views.fnadd_user,name="add_user"),
    path('disable_user/<userdis_id>',views.fndisable_user,name="disable_user"),
    path('edit_user/<useredit_id>',views.fnedit_user,name="edit_user"),

    path('paths/',views.fnpath,name="paths"),
    path('add_path/',views.fnaddpath,name="add_path"),
    path('edit_path/<pathedit_id>',views.fnedit_path,name="edit_path"),
    path('disable_path/<pathdis_id>',views.fndisable_path,name="disable_path"),

    path('brands/',views.fnbrand,name="brands"),
    path('add_brand/',views.fnadd_brand,name="add_brand"),
    path('edit_brand/<brandedit_id>',views.fnedit_brand,name="edit_brand"),
    path('disable_brand/<branddis_id>',views.fndisable_brand,name="disable_brand"),

    path('color/',views.fncolor,name="color"),
    path('add_color/',views.fnadd_color,name="add_color"),
    path('edit_color/<editcolor_id>',views.fnedit_color,name="edit_color"),
    path('disable_color/<colordis_id>',views.fndisable_color,name="disable_color"),
]
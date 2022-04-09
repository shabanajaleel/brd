from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model


# Create your views here.
context={}


def fnlogin(request):
    if request.method=="POST":
        employee_id=request.POST['employee']
        password=request.POST['password']
        user=authenticate(employee_id=employee_id,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect(fnhome)
    return render(request,'login.html')

def fnlogout(request):
    logout(request)
    return redirect(fnlogin)



def fnhome(request):
    return render(request,'home.html')




# Roles
def fnroles(request):
    roles=Role.objects.all()
    context['roles']=roles
    if request.method=="POST":
        role=request.POST['role']
        status=request.POST['status']
        if role:
            roles=roles.filter(role=role)
            context['roles']=roles
 
        if status:
            roles=roles.filter(status=status)
            context['roles']=roles

    return render(request,'Users/Role/roles.html',context)

def fnadd_roles(request):
    form=RoleForm()
    context['form']=form

    if request.method=="POST":
        form=RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Role added successfully')
            return render(request,'Users/Role/roles.html')
            
        else:
            form=RoleForm()
            context['form']=form

    return render(request,'Users/Role/addrole.html',context)

def fndisable_roles(request,roledis_id):
    roles=Role.objects.get(id=roledis_id)
    if roles.status== "Active":
        roles.status ='Inactive'
        roles.save()
        return redirect(fnroles)
    else:
        roles.status ='Active'
        roles.save()
        return redirect(fnroles)

def fnedit_roles(request,editrole_id):
    roles=Role.objects.get(id=editrole_id)
    form=RoleForm(request.POST or None,instance=roles)
    context['form']=form

    if form.is_valid():
        form.save()
        messages.success(request,'Role Edited successfully')
        return redirect(fnroles)
        
    return render(request,'Users/Role/addrole.html',context)

def fnadd_permissions(request,perm_id):
    path=Path.objects.filter(status="Active",parent=None)
    context['path']=path

    if request.method=="POST":
        perm=request.POST.getlist('sub_perm')
        mainperm=request.POST.getlist('main_perm')
        addperm=Role.objects.get(id=perm_id)
        addperm.permissions.clear()
        print( addperm.permissions)
        for i in perm:
            addperm.permissions.add(Path.objects.get(id=i))
        for j in mainperm:
            addperm.permissions.add(Path.objects.get(id=j))
        messages.success(request,'permissions added successfully')
        return redirect(fnroles)

    permission=[i.id for i in  Role.objects.get(id=perm_id).permissions.all()]
    print(permission)
    context['permission']=permission

    return render(request,'Users/Role/addpermission.html',context)


# end role

# user
def fnusers(request):
    users=CustomUser.objects.all()
    context['users']=users
    if request.method=="POST":
        employee_id=request.POST['employee_id']
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        status=request.POST['status']
        district=request.POST['district']

        if employee_id:
            users=users.filter(employee_id__icontains=employee_id)
            context['users']=users

        if name:
            users=users.filter(first_name__icontains=name)
            context['users']=users

        if phone:
            users=users.filter(phone__icontains=phone)
            context['users']=users
        
        if role:
            users=users.filter(role__icontains=role)
            context['users']=users
        
        if status:
            users=users.filter(status__icontains=status)
            context['users']=users

        if district:
            users=users.filter(district__icontains=district)
            context['users']=users

    return render(request,'Users/User/users.html',context)

def fnadd_user(request):
    form=CustomUserForm
    context['form']=form
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User added successfully')
            return redirect(fnusers)
        else:
            print(form.errors)
            context['form']=form
            return render (request,'Users/User/adduser.html',context)
            
    return render (request,'Users/User/adduser.html',context)

def fndisable_user(request,userdis_id):
    users=CustomUser.objects.get(id=userdis_id)
    if users.status== "Active":
        users.status ='Inactive'
        users.save()
        return redirect(fnusers)
    else:
        users.status ='Active'
        users.save()
        return redirect(fnusers)

def fnedit_user(request,useredit_id):
    users=CustomUser.objects.get(id=useredit_id)
    form=EditUserForm(request.POST or None,instance=users)
    context['form']=form

    if form.is_valid():
        form.save()
        messages.success(request,'User Edited successfully')
        return redirect(fnusers)
        
    return render(request,'Users/User/edituser.html',context)


# end user

# path
def fnpath(request):
    paths=Path.objects.all()
    if request.method=="POST":
        path=request.POST['path']
        status=request.POST['status']
        if path:
            paths=paths.filter(path_name__icontains=path)
        if status:
            paths=paths.filter(status=status)

    context['path']=paths
    return render(request,'Users/Path/path.html',context)

def fnaddpath(request):
    form=PathForm
    context['form']=form
    if request.method=="POST":
        form=PathForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Path added successfully')
            return redirect(fnpath)
        else:
            context['form']=form
            return render(request,'Users/Path/addpath.html',context)

    return render(request,'Users/Path/addpath.html',context)

def fnedit_path(request,pathedit_id):
    paths=Path.objects.get(id=pathedit_id)
    form=PathForm(request.POST or None,instance=paths)
    context['form']=form

    if form.is_valid():
        form.save()
        messages.success(request,'Path Edited successfully')
        return redirect(fnpath)
        
    return render(request,'Users/Path/addpath.html',context)

def fndisable_path(request,pathdis_id):
    paths=Path.objects.get(id=pathdis_id)
    if paths.status== "Active":
        paths.status ='Inactive'
        paths.save()
        return redirect(fnpath)
    else:
        paths.status ='Active'
        paths.save()
        return redirect(fnpath)


# endpath

# brand
def fnbrand(request):
    brand=Brand.objects.all()
    context['brand']=brand
    if request.method=="POST":
        brand_name=request.POST['brand']
        status=request.POST['status']
        
        if brand_name:
            brand=brand.filter(brand_name__icontains=brand_name)
            context['brand']=brand

        if status:
            brand=brand.filter(status=status)
            context['brand']=brand

    return render(request,'Brand/brands.html',context)

def fnadd_brand(request):
    form=BrandForm
    context['form']=form
    if request.method=="POST":
        form=BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Brand Added Successfully ')
            return redirect(fnbrand)
        else:
            context['form']=form
            return render(request,"Brand/addbrand.html",context)

    return render(request,"Brand/addbrand.html",context)

def fnedit_brand(request,brandedit_id):
    brand=Brand.objects.get(id=brandedit_id)
    form=BrandForm(request.POST or None,instance=brand)
    context['form']=form

    if form.is_valid():
        form.save()
        messages.success(request,'Brand Edited successfully')
        return redirect(fnbrand)
        
    return render(request,'Brand/addbrand.html',context)

def fndisable_brand(request,branddis_id):
    brand=Brand.objects.get(id=branddis_id)
    if brand.status== "Active":
        brand.status ='Inactive'
        brand.save()
        return redirect(fnbrand)
    else:
        brand.status ='Active'
        brand.save()
        return redirect(fnbrand)
# endbrand

# color
def fncolor(request):
    color=Color.objects.all()
    context['color']=color
    if request.method=="POST":
        color_name=request.POST['color']
        status=request.POST['status']
        
        if color_name:
            color=color.filter(color__icontains=color_name)
            context['color']=color

        if status:
            color=color.filter(status=status)
            context['color']=color

    return render(request,'Color/color.html',context)

def fnadd_color(request):
    form=ColorForm
    context['form']=form
    if request.method=="POST":
        form=ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Color Added Successfully ')
            return redirect(fncolor)
        else:
            context['form']=form
            return render(request,"Color/addcolor.html",context)

    return render(request,"Color/addcolor.html",context)

def fnedit_color(request,editcolor_id):
    color=Color.objects.get(id=editcolor_id)
    form=ColorForm(request.POST or None,instance=color)
    context['form']=form

    if form.is_valid():
        form.save()
        messages.success(request,'Color Edited successfully')
        return redirect(fncolor)
        
    return render(request,'Color/addcolor.html',context)

def fndisable_color(request,colordis_id):
    color=Color.objects.get(id=colordis_id)
    if color.status== "Active":
        color.status ='Inactive'
        color.save()
        return redirect(fncolor)
    else:
        color.status ='Active'
        color.save()
        return redirect(fncolor)
# endcolor
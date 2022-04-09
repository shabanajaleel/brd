from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class Path(models.Model):
    path_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    parent=models.ForeignKey('Path',on_delete=models.CASCADE,null=True,blank=True)
    Created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Path'
        ordering = ['-Created_at']

    def __str__(self):
        return self.path_name



class Role(models.Model):
    role=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default='Active',choices=(
        ('Active','Active'),
        ('Inactive','Inactive'),
    ))
    permissions=models.ManyToManyField(Path,null=True,blank=True)
    Created_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = 'Role'
        ordering = ['-Created_at']

    def __str__(self):
        return self.role

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,employee_id, email, password, **extra_fields):
        '''Create and save a user with the given email, and
        password.
        '''
        if not employee_id:
            raise ValueError('The embloyee id must be set')
        if not email:
            raise ValueError('The email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,employee_id, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self._create_user(employee_id,email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100,unique=True) 
    phone=models.BigIntegerField(null=True)  
    district=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=30)  
    role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
    usertype=models.CharField(max_length=20,choices=(
        ('Salesman','Salesman'),
        ('Evaluator','Evaluator'),
        ('Callcentre','callcentre'),
        ('Admin','Admin'),
    ),null=True,blank=True)
    target=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ),null=True,blank=True)
    Created_at = models.DateTimeField(auto_now=True)
    
    
    objects = UserManager()
    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'CustomUser'
        ordering = ['-Created_at']

    def __str__(self):
        return self.first_name
    
class Brand(models.Model):
    brand_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Brand'
        ordering = ['-Created_at']

    def __str__(self):
        return self.brand_name

class Color(models.Model):
    color=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Color'
        ordering = ['-Created_at']

    def __str__(self):
        return self.color
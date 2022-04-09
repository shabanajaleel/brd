from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
import re


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_REGEX="^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('first_name','employee_id','phone','district','password1','password2','email','role','usertype','target')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def save(self,commit=True):
        user=super(CustomUserForm,self).save(commit=False)
        user.role=self.cleaned_data['role']
        user.phone=self.cleaned_data['phone']
        user.employee_id=self.cleaned_data['employee_id']
        user.district=self.cleaned_data['district']
        user.email=self.cleaned_data['email']
        user.usertype=self.cleaned_data['usertype']
        user.target=self.cleaned_data['target']
        if commit:
            user.save()
            return user

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and not re.match(EMAIL_REGEX, str(email)):
            raise forms.ValidationError('Invalid email format')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone and not re.match(PHONE_REGEX,str(phone))  :
            raise forms.ValidationError('Invalid phone Number')

        return phone


class EditUserForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('first_name','employee_id','phone','district','email','role','usertype','target')
    
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def save(self,commit=True):
        user=super(EditUserForm,self).save(commit=False)
        user.role=self.cleaned_data['role']
        user.phone=self.cleaned_data['phone']
        user.employee_id=self.cleaned_data['employee_id']
        user.district=self.cleaned_data['district']
        user.email=self.cleaned_data['email']
        user.usertype=self.cleaned_data['usertype']
        user.target=self.cleaned_data['target']
        if commit:
            user.save()
            return user
 

class RoleForm(forms.ModelForm):
    class Meta:
        model=Role
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})


class PathForm(forms.ModelForm):
    class Meta:
        model=Path
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(PathForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})


class ColorForm(forms.ModelForm):
    class Meta:
        model=Color
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
from django import forms


class SignUpForm(forms.Form):
    Full_Name = forms.CharField(max_length = 200)
    Full_Name.widget.attrs.update({'class': 'form-control form-control-lg'})  
    
    Email = forms.EmailField(max_length=200)
    Email.widget.attrs.update({'class': 'form-control form-control-lg'})  
    
    Password = forms.CharField(widget = forms.PasswordInput())
    Password.widget.attrs.update({'class': 'form-control form-control-lg'})  

from django import forms


class loginForm(forms.Form):
    Email = forms.EmailField(max_length=200)
    Email.widget.attrs.update({'class': 'form-control form-control-lg'})  
    
    Password = forms.CharField(widget = forms.PasswordInput())
    Password.widget.attrs.update({'class': 'form-control form-control-lg'})  

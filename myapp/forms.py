from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

from myapp.models import Posts


class SignupForm(UserCreationForm):
        password1 = forms.CharField(label='password', widget=forms.PasswordInput (attrs={'class':'form-control'}))  
        password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput (attrs={'class':'form-control'})) 
        
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email',]
            labels = {'first_name':'Fisrt Name','last_name':'Last Name','email':'Email'}
            widgets = {
                 'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.TextInput(attrs={'class':'form-control'})
            }
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password =forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))

class AddForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','description','profileimg']
        labels = {'title':'Title','description':'Description','profileimg':'Images'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

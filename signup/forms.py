from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(label="Name", max_length=250)
    email_address = forms.EmailField(label="Email ID", max_length=250)  
    username = forms.CharField(label="Username", max_length=250)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=250)  

class LogInForm(forms.Form):
    username = forms.CharField(label="Username", max_length=250)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=250)  

    

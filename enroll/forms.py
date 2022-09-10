from django import forms
from .models import User

class StudentsRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name Here...'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email Here...'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'placeholder':'Enter Your Password Here...'}),
        }
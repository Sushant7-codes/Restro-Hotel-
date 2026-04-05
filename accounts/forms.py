from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'age', 'location']
    
    # Add this method to check if email already exists
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean_age(self):
        age= self.cleaned_data.get('age')
        if age<0:
            raise forms.ValidationError("Age cannot be negative.")
        elif age>130:
            raise forms.ValidationError("Age cannot be greater than 130.")
        return age

from django import forms
from .models import Account, UserProfile


class RegistrationFrom(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationFrom,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    def clean(self):
        clean_data = super(RegistrationFrom, self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.forms.ValidationError(
                "Password doesn't match!"
            ) 

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    
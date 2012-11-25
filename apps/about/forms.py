from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'My First Video'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe your video... (You can always edit it later.)','rows': 3}))
    uuid = forms.CharField(widget=forms.HiddenInput)
    price = forms.DecimalField(decimal_places=2, widget=forms.TextInput(attrs={'placeholder': '1.00', 'class':'span1'}))
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=250)
    paypal_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'mypaypal@email.com'}), label='PayPal Email',help_text='Payments will be sent here.')
    password = forms.CharField(max_length=250, widget=forms.PasswordInput)
    password_again = forms.CharField(max_length=250, widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'%s already exists' % username )

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']

        if password != password_again:
             raise forms.ValidationError('Passwords do not match')

     return self.cleaned_data['password_again']

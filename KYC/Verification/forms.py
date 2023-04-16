from django import forms
from django.core import validators
from .apis import pan_verifiy

class VerificationForm(forms.Form):
    pan = forms.CharField(label="Enter PAN Card Number:")


    def clean(self):
        all_data = super().clean()
        pan = all_data['pan']
        print('pancard No------>:',pan)
        pan_verifiy(pan)

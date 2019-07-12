from .models import ContactMessage
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'geekschurch@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+12) 123 456 7910'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'name': 'message', 'cols': '30', 'rows': '10',
                                              'placeholder': 'Message'})
        }

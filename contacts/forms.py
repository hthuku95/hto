from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
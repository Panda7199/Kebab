from django import forms
from home.models import ContactMessage, Comment_cheff


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ( 'name', 'surname', 'email', 'phone',  'message',)

class Comment_detail_Form(forms.ModelForm):
    class Meta:
        model = Comment_cheff
        fields = ( 'name' ,'email' ,'comment',)
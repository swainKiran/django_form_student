from django import forms
#from .models import Student

g = [('sports', 'Sports'), ('music', 'Music'), ('art', 'Art')]
c = [('public', 'Public'), ('private', 'Private'), ('charter', 'Charter')]

class studentInfo(forms.Form):
    sname = forms.CharField(max_length=100)
    sage = forms.IntegerField(min_value=5)
    semail = forms.EmailField()
    spassword = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(widget=forms.Textarea)
    hubby = forms.MultipleChoiceField(choices=g, widget=forms.CheckboxSelectMultiple)
    school_type = forms.ChoiceField(choices=c, widget=forms.RadioSelect)
    school_logo = forms.FileField(label="School Logo")




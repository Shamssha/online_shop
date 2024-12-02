from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام را وارد کنید'})
        ,label_suffix='', label='نام'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید.'})
        , required=True, label_suffix='', label="ایمیل")
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'پیام خود را وارد کنید.',})
        ,required=True, label_suffix='', label='پیام')
   
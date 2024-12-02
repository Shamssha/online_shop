from django import forms

class UserNewOrder(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(attrs={'class':'form-control'})
        )
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class':'form-control w-25 list-inline-item mb-25', 'placeholder':'مقدار'}), 
        initial= 0
        )
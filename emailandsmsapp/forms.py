from django import forms
from.models import RegModel
class RegForm(forms.ModelForm):
    class Meta:
        model=RegModel
        fields=['FName','LName','UName','Password','CPassword', 'Email','Mobno']
        widgets = {'password': forms.PasswordInput(),
                   'CPassword': forms.PasswordInput()}
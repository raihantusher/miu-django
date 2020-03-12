from django import forms

class NameForm(forms.Form):
    set_uuid = forms.CharField( max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                
                                }))
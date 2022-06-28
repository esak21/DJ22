
from django import forms
from django.contrib import admin
from .models import TicketModel


class TicketAdminForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-c3'})
        # we can update the palceholder as below for all the Fields 
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {   'placeholder': f'Ticket-{str(field)}',
                    
                },
                
                )

    # Changing the Fields 
    description = forms.CharField(
        widget= forms.Textarea(
            attrs= {
                "class": "text-2xl border-3",
                "placeholder": "enter the description",
                "rows": 3,
            }
        )
    )

    class Meta:
        model=TicketModel
        fields ="__all__"

    def clean_title(self):
        if self.cleaned_data['title'] == 'admin':
            raise forms.ValidationError("No WAY YOU CALLED ADMIN")
        return self.cleaned_data['title']

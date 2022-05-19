
from django.forms import ModelForm
from .models import Project
from django import forms


# Django will Look for the Project Model and create it automatically 
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','demo_link','source_link','tags','featured_image']


        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs) -> None:
        super(ProjectForm, self).__init__(*args, **kwargs)

        for k,v in self.fields.items():
            self.fields[k].widget.attrs.update({
                'class': 'input'
            })

        # this way we need to put all of our columns 
        # self.fields['title'].widget.attrs.update(
        #     {
        #         'class': 'input',
        #         'placeholder': 'AddTitle'

        #     })

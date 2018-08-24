from django import forms
from .models import Skill


class AdviceForm(forms.ModelForm):
    advices = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,
                                                           'cols': 100}),
                              required=False)

    class Meta:
        model = Skill
        fields = ('__all__')


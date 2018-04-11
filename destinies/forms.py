from django import forms

from pagedown.widgets import PagedownWidget

from .models import Destiny
from accounts.models import User

class DestinyForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), 
                                  empty_label="(Nothing)")
    class Meta:
        model = Destiny
        fields = [
            "name",
            "address",
            "details",
            "user"
        ]
  
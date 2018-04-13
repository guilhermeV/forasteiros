from django import forms

from pagedown.widgets import PagedownWidget

from .models import Event
from destinies.models import Destiny

class EventForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.SelectDateWidget)
    final_date = forms.DateField(widget=forms.SelectDateWidget)
    destiny = forms.ModelChoiceField(queryset=Destiny.objects.all(),
                                  empty_label="(Nothing)")

    class Meta:
        model = Event
        fields = [
            "title",
            "destiny",
            "initial_date",
            "final_date",
            "details",
            "payment_options",
            "meeting_point",
            "status",
        ]
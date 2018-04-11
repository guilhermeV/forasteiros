from django import forms

from pagedown.widgets import PagedownWidget

from .models import Event

class EventForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.SelectDateWidget)
    final_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Event
        fields = [
            "title",
            "initial_date",
            "final_date",
            "details",
            "payment_options",
            "meeting_point",
            "status",
        ]
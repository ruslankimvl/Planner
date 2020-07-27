import django.forms as forms

from Blog.models import Meeting
from Blog.models import Room


class CreationForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'title',
            'date',
            'start_time',
            'duration',
            'room'
        ]

class CreationForm_Room(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'floor',
            'room_number'
        ]

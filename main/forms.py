from django.forms import ModelForm
from main.models import *


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = "__all__"

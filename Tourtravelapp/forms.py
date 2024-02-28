
from Tourtravelapp.models import Pakage
from django.forms import Form, ModelForm

class Viewpakages(ModelForm):
    class Meta:
        model = Pakage
        fields = '__all__'
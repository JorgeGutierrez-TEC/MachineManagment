from django.forms import ModelForm
from .models import Status, BancoEm

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'description', 'is_active']

class BancoForm(ModelForm):
    class Meta:
        model = BancoEm
        fields = ['dinero']

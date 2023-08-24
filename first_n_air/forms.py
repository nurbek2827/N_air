from django import forms
from first_n_air.models import Buy


class ChoisesForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ["product"]
        fields = "__all__"
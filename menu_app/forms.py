from django import forms
import re


class IceCreamForm(forms.Form):
    ice_cream_name = forms.CharField()
    ice_cream_flavour = forms.CharField()
    ice_cream_weight = forms.IntegerField()

    def clean_ice_cream_weight(self):
        weight = self.cleaned_data.get('ice_cream_weight')
        if weight <= 0:
            raise forms.ValidationError("Ice Cream Weight must be a positive number.")
        return weight

    def clean_ice_cream_flavour(self):
        flavour = self.cleaned_data.get('ice_cream_flavour')
        if not re.match("^[a-zA-Z\s]+$", flavour):
            raise forms.ValidationError("Ice Cream Flavour must contain only letters.")
        return flavour

    def clean_ice_cream_name(self):
        name = self.cleaned_data.get('ice_cream_name')
        if not re.match("^[a-zA-Z\s]+$", name):
            raise forms.ValidationError("Ice Cream Name must contain only letters.")
        return name

class UpdateIceCreamForm(forms.Form):
    ice_cream_id = forms.IntegerField()
    ice_cream_name = forms.CharField()
    ice_cream_flavour = forms.CharField()
    ice_cream_weight = forms.IntegerField()

    def clean_ice_cream_weight(self):
        weight = self.cleaned_data.get('ice_cream_weight')
        if weight <= 0:
            raise forms.ValidationError("Ice Cream Weight must be a positive number.")
        return weight

    def clean_ice_cream_flavour(self):
        flavour = self.cleaned_data.get('ice_cream_flavour')
        if not re.match("^[a-zA-Z\s]+$", flavour):
            raise forms.ValidationError("Ice Cream Flavour must contain only letters.")
        return flavour

    def clean_ice_cream_name(self):
        name = self.cleaned_data.get('ice_cream_name')
        if not re.match("^[a-zA-Z\s]+$", name):
            raise forms.ValidationError("Ice Cream Name must contain only letters.")
        return name
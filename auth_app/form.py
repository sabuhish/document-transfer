from django.contrib.auth.forms import UserCreationForm
from companies_app.models import Company
from django.forms import ModelForm

class RegisterCompany(UserCreationForm):
    fields= ["username", "email", ]

class CompanyCreatefrom(ModelForm):
    class Meta:
        model= Company
        fields = ["voen", "name", "ceo_first_name", "ceo_lastname"]



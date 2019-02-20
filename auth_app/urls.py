from django.urls import path
from .views import *

urlpatterns = [
    path("register/",Companyregister.as_view(), name="company_register" )
]


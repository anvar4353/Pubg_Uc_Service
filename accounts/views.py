from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# lOGIN VA SIGNUP QISIM UN CLASS
class UserCreationView(CreateView):
    # Login va parol formasi tayor form_class ga beradi
    form_class = UserCreationForm
    
    # Login va parol formasi tayor signup.html ga beradi
    template_name = 'signup.html'

    # Royxatdan o'tkandan keyingi yo'naltirilishi
    success_url = reverse_lazy("login")

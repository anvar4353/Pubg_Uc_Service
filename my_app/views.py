from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import *
import requests
import json



class IndexPageView(TemplateView):
	template_name = 'index.html'



# requests kutubxonasi import qilinadi
import requests

# Telegram bot orqali xabar jo'natish funksiyasi
def telegram_bot_sendtext(bot_message):
    # Botning tokeni
    bot_token = '6222799852:AAFi9F-CBVAJHD5FTkiCdEFqsiOHZpOJ0GU'
    
    # Qabul qiluvchi (user) id raqami
    bot_chatID = '503581054'
    
    # Xabar jo'natish uchun URL
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
    
    # Xabar jo'natish so'rovi
    response = requests.get(send_text)
    
    # Xabar jo'natilganini tekshirish (kerakmasa, o'rniga yuborilgan xabar haqida ma'lumot beradi)
    return response.json()

# SmsView funksiyasi
def SmsView(request):
    if request.method == 'POST':
        # Forma orqali kiritilgan ma'lumotlarni olish
        ism = request.POST.get('name', None)
        tel = request.POST.get('tel', None)
        email = request.POST.get('email', None)
        sms = request.POST.get('sms', None)
        
        # Sms modelini yaratish va saqlash
        user = Sms.objects.create(
            UserName=ism,
            tel=tel,
            email=email,
            sms=sms
        )
        user.save()
        
        # Xabar jo'natish
        telegram_bot_sendtext(f"Ism: {ism},\nTelefon raqam: {tel}\nEmail: {email}\nXabar: {sms}")
    
    # Shablonni yuborish
    return render(
        request=request,
        template_name='sms.html'
    )

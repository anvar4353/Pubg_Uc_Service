from django.db import models

class Sms(models.Model):
    UserName = models.CharField(max_length=250, blank=True, null=True)  # Foydalanuvchi nomi, bo'sh qoldirilish ruxsat beriladi
    tel = models.CharField(max_length=20)  # Telefon raqami
    email = models.CharField(max_length=50)  # Elektron pochta manzili
    sms = models.TextField(blank=True, null=True)  # SMS matni
    Date = models.DateTimeField(auto_now_add=True)  # Sana va vaqt, avtomatik ravishda qo'shiladi

    def __str__(self):
        return self.UserName

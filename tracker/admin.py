from django.contrib import admin
from .models import UserProfile, DailyProgress, CustomTask

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_xp', 'streak_days', 'language']

@admin.register(DailyProgress)
class DailyProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'fajr', 'dhuhr', 'asr', 'maghrib', 'isha', 'quran_pages']
    list_filter = ['date', 'user']

@admin.register(CustomTask)
class CustomTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'label', 'done']

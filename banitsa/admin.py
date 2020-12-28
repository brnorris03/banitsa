from django.contrib import admin

from .models import Fortune

class FortuneAdmin(admin.ModelAdmin):
    list_display = ['id','fortune_text', 'english_text', 'pub_date']


admin.site.register(Fortune, FortuneAdmin)

from django.contrib import admin
from .models import *


# admin.site.register(CreateCustomer)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)


class OptionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'option', 'is_correct', 'user_answer')
    

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Option, OptionAdmin)
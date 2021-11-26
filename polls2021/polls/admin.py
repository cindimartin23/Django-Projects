from django.contrib import admin
from django.db import models
from .models import Question, Choice

admin.site.site_header = "Administrador de Encuestas"
admin.site.site_title = "Area de Administración de Encuestas"
admin.site.index_title = "Bienvenido al Area de Administración de Encuestas"

# Personalizando el Admin Form
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
# Register your models here.
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
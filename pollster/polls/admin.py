from django.contrib import admin

# Brings in the models
from .models import Question, Choice

# Changes the site header
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 62


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['publish_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

# Register the models
# admin.site.register(Question)
# admin.site.register(Choice)


# Registers the classes above
admin.site.register(Question, QuestionAdmin)

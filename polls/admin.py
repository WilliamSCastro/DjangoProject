from django.contrib import admin

# Register your models here.


from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently", "numero_opcions"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    def numero_opcions(self, obj):
        return obj.choice_set.count()


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

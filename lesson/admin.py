from django.contrib import admin

from lesson.models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "hour_count",
        "date",
        "time",
    )


admin.site.register(Lesson, LessonAdmin)

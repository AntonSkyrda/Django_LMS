from django.contrib import admin

from task.models import Task, Submission


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "due_date",
    )


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("graded",)


admin.site.register(Task, TaskAdmin)
admin.site.register(Submission, SubmissionAdmin)

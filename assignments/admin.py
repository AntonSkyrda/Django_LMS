from django.contrib import admin

from assignments.models import TeachingAssignment


class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "teacher",
        "course",
        "group",
    )


admin.site.register(TeachingAssignment, TeachingAssignmentAdmin)

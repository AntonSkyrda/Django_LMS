from django.contrib import admin

from course.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "teacher",
    )


admin.site.register(Course, CourseAdmin)

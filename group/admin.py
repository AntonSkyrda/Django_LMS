from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "course_number",
    )


admin.site.register(Group, GroupAdmin)

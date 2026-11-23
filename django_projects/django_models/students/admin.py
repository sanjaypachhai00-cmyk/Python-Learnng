
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Columns displayed in the student list
    list_display = (
        'id',
        'name',
        'email',
        'age',
        'course',
        'phone',
    )

    # Clickable field to open student details
    list_display_links = (
        'id',
        'name',
    )

    # Search functionality
    search_fields = (
        'name',
        'email',
        'course',
        'phone',
    )

    # Filters on the right side
    list_filter = (
        'age',
        'course',
    )

    # Default ordering
    ordering = ('id',)

    # Number of records per page
    list_per_page = 10

    # Organize fields when adding or editing students
    fieldsets = (
        ('Personal Information', {
            'fields': (
                'name',
                'email',
                'age',
                'phone',
            )
        }),

        ('Academic Information', {
            'fields': (
                'course',
            )
        }),
    )

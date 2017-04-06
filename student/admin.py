from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from student.models import Student

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["name", "rollno", "batch",
                    "gender", "current_CGPA",
                    "fathers_name"]
    search_fields = ["name", "rollno"]
    list_display_links = ["name"]

    class Meta:
        model = Student

admin.site.register(Student, StudentModelAdmin)

from django.contrib import admin
from job.models import Job, AppliedJob


class JobModelAdmin(admin.ModelAdmin):
    list_display = ["company", "minimum_cgpa"]
    search_fields = ["company_id", "company"]
    list_display_links = ["company"]

    class Meta:
        model = Job

class AppliedJobModelAdmin(admin.ModelAdmin):
    list_display = ["student_rollno", "student_applied_job"]
    search_fields = ["student_applied_job"]
    list_display_links = ["student_rollno"]

    class Meta:
        model = AppliedJob


admin.site.register(Job, JobModelAdmin)
admin.site.register(AppliedJob, AppliedJobModelAdmin)

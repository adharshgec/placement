from django.contrib import admin
from result.models import Result

class ResultModelAdmin(admin.ModelAdmin):
    list_display = ["result_detail", "published_date"]
    search_fields = ["result_detail", "published_date"]
    list_display_links = ["result_detail"]

    class Meta:
        model = Result

admin.site.register(Result, ResultModelAdmin)

from django.contrib import admin
from django.db.models import Avg

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_author', 'average_score_display')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(avg_score=Avg('rating__score'))

    def average_score_display(self, obj):
        return round(obj.avg_score or 0, 2)
    average_score_display.short_description = '평균 평점'
    average_score_display.admin_order_field = 'avg_score'

admin.site.register(Project, ProjectAdmin)
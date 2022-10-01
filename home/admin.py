from django.contrib import admin
from .models import Commit


class CommitAdmin(admin.ModelAdmin):
    list_display = ('date', 'msg')


admin.site.register(Commit, CommitAdmin)

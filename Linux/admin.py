from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')


admin.site.register(Member, MemberAdmin)

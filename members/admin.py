from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member
from .models import Section, Year, Department, MEMBER_TYPE

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('card', 'name', 'section', 'year', 'member_type', 'department')
    search_fields = ('card', 'name', 'section__sec', 'year__session', 'department__dept', 'member_type')

    list_filter = ("member_type", "section__sec", "year__session", 'department__dept')


admin.site.register(Member, MemberAdmin)
admin.site.register(Section)
admin.site.register(Year)
admin.site.register(Department)

from django.contrib import admin
from .models import test,demo


class TestModelAdmin(admin.ModelAdmin):
    list_display= ('firstname','lastname','DOJ')  

admin.site.register(test, TestModelAdmin)


class New(admin.ModelAdmin):
    list_display = ('department','salary')

admin.site.register(demo ,New)    



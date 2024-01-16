from django.contrib import admin
from .models import year,subject,student,result
# Register your models here.
admin.site.register(year)
admin.site.register(subject)
admin.site.register(student)
admin.site.register(result)
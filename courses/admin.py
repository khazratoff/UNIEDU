from statistics import mode
from django.contrib import admin
from courses import models
# Register your models here.
admin.site.register(models.Courses)
admin.site.register(models.Comments)
admin.site.register(models.Tags)

from django.contrib import admin

# Register your models here.
from .models import Student, Article


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class CourseAdmin(admin.ModelAdmin):
    pass
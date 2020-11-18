from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Content)


# from .models import Subject, Course, Module
# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug']
#     prepopulated_fields = {'slug': ('title',)}
#
# #
# # class ModuleInline(admin.StackedInline):
# #     model = Module
#
#
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['title', 'subject', 'created']
#     list_filter = ['created', 'subject']
#     search_fields = ['title', 'overview']
#     prepopulated_fields = {'slug': ('title',)}
#     # inlines = [ModuleInline]
#
# # @admin.register(Course)
# # class CourseAdmin(admin.ModelAdmin):
# #     list_display = ['title', 'slug']
# #     prepopulated_fields = {'slug': ('title',)}
#
# # @admin.register(Module)
# # class ModuleAdmin(admin.ModelAdmin):
# #     list_display = ['title', 'slug']
# #     prepopulated_fields = {'slug': ('title',)}

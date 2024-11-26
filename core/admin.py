from django.contrib import admin

from core.models import Comment, Car

admin.site.register(Car)
admin.site.register(Comment)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields = ["__all__"]
from django.contrib import admin
from . models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'github','skills')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
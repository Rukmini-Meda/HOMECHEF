from django.contrib import admin
from .models import Profile, VolunteerModel

class VolunteerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'address',
        'city',
        'state',
        'pincode',
        
    ]
    search_fields = ['zip'] 


admin.site.register(Profile)
admin.site.register(VolunteerModel)
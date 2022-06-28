from django.contrib import admin
from django.forms import Textarea
from .models import TicketingUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TicketinguserAdminConfig(UserAdmin):
    
    model = TicketingUser

    search_fields = ('email', 'name',)
    list_filter = ('email',)
    ordering = ('created_at', )
    list_display = ('email', 'name', 'lastname', 'mobileno','is_active', 'is_superuser' )

    # Displaying Fields 
    fieldsets = (
        ('LoginDetails', {'fields': ('email', 'name', 'lastname', 'password')}),
        ('permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('personalDetails', {'fields': ('mobileno', 'description','userimage')}),
    )

    formfield_overrides = {
        TicketingUser.description : {'widget': Textarea(attrs= {
            'rows': 5, 
            'cols': 5
        })}, 
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide', ), 
            'fields': ('email', 'name', 'lastname', 'mobileno', 'description','userimage', 'password1', 'password2', 'is_staff','is_superuser' )
        }),
    )







#21395318


admin.site.register(TicketingUser, TicketinguserAdminConfig)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

'''
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
'''

admin.site.register(CustomUser)
admin.site.register(Transaction)
admin.site.register(Product)
admin.site.register(SchoolAttend)

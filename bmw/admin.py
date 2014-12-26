from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import UserProfile
from models import Center

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

class MyUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


#to make Center
class CenterAdmin(admin.ModelAdmin):
	fields = ['place', 'name']

admin.site.register(Center, CenterAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Student, Teacher
from .forms import UserCreationForm

class UserAdmin(BaseUserAdmin):
    model = User
    add_form = UserCreationForm
    fieldsets = (
        *BaseUserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'middle_name',
                    'image',
                    'phone'
                )
            }
        )
    )


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Category, Product


# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    fields = ('AccountType', 'email', 'password', 'username')


admin.site.register(Category)
admin.site.register(Product)
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)

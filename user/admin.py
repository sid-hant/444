from django.contrib import admin
from .models import User, Ban
# Register your models here.
admin.site.register(User)
admin.site.register(Ban)
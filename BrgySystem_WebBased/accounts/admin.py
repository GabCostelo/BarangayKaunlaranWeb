from django.contrib import admin
from .models import User,BrgyStaff,Constituent
# Register your models here.

admin.site.register(User)
admin.site.register(BrgyStaff)
admin.site.register(Constituent)

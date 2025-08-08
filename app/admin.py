from django.contrib import admin
from .models import InteriorWork
# Register your models here.


admin.site.site_header = "Fitspace Admin"
admin.site.site_title = "Fitspace Admin Portal"
admin.site.index_title = "Welcome to Fitspace Admin Portal"

admin.site.register(InteriorWork)
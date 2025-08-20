from django.contrib import admin
from .models import InteriorWork,GalleryImage,Blog,Featured_Blog,banner_Image
# Register your models here.


admin.site.site_header = "Fitspace Admin"
admin.site.site_title = "Fitspace Admin Portal"
admin.site.index_title = "Welcome to Fitspace Admin Portal"

admin.site.register(InteriorWork)
admin.site.register(GalleryImage)
admin.site.register(Blog)
admin.site.register(Featured_Blog)
admin.site.register(banner_Image)


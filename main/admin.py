from django.contrib import admin

from .models import Photos,Users,Comment,Like,Connection

# Register your models here.


admin.site.register(Photos)
admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Connection)

from .models import UploadedImage
admin.site.register(UploadedImage)

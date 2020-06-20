from django.contrib import admin

from .models import Photos,Users,Comment,Like,Connection,Tags,TagHash

# Register your models here.


admin.site.register(Photos)
admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Connection)
admin.site.register(Tags)
admin.site.register(TagHash)

from .models import UploadedImage
admin.site.register(UploadedImage)

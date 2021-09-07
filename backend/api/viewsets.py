from rest_framework import viewsets, filters
from .serializers import UploadedImageSerializer
from main.models import UploadedImage







class UploadedImagesViewSet(viewsets.ModelViewSet):
    
    queryset = UploadedImage.objects.all()
    print(UploadedImageSerializer)

    serializer_class = UploadedImageSerializer





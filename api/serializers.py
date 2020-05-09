from main.models import Users,Photos,Comment,Like
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields ='__all__'


class PhotosSerializer(serializers.ModelSerializer):

    username=serializers.CharField(max_length=20)

    class Meta:
        model=Photos
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):

    username=serializers.CharField(max_length=20)
    profile_img=serializers.ImageField()

    

    class Meta:
        model=Comment
        fields='__all__'


class LikeSerializer(serializers.ModelSerializer):

    username=serializers.CharField(max_length=20)
    profile_img=serializers.ImageField()

    

    class Meta:
        model=Like
        fields='__all__'
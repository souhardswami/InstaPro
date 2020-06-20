from django.db import models

# Create your models here.






class Users(models.Model):
    name=models.CharField(max_length=20,null=False)
    username=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=30)
    profile_img=models.ImageField(upload_to='pics/',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    # followers = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username




class Photos(models.Model):
    image_url=models.ImageField(upload_to='pics/')
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True)
    tag=models.TextField()


    def __str__(self):
        return self.tag



class Comment(models.Model):
    comment_text=models.CharField(max_length=250)
    user=models.ForeignKey(Users,null=True,on_delete=models.SET_NULL)
    photo=models.ForeignKey(Photos,null=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)
    parent=models.OneToOneField("self",blank=True,on_delete=models.CASCADE,null=True)



class Like(models.Model):
    photo=models.ForeignKey(Photos,null=True,on_delete=models.SET_NULL)
    user=models.ForeignKey(Users,null=True,on_delete=models.SET_NULL)





class TagHash(models.Model):
    tagword=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.tagword


class Tags(models.Model):
    tagpar=models.ForeignKey(TagHash,null=True,on_delete=models.CASCADE)
    photo=models.ForeignKey(Photos,null=True,on_delete=models.SET_NULL)


class Connection(models.Model):
    user = models.ForeignKey(Users, related_name='following',on_delete=models.CASCADE)
    follower = models.ForeignKey(Users, related_name='follower',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower}     ->   -> ->  {self.user}'



















class UploadedImage(models.Model):
    """
    Provides a Model which contains an uploaded image aswell as a thumbnail
    """
    image = models.ImageField("Uploaded image", upload_to="fake/")

    
    # title and description
    
    

    
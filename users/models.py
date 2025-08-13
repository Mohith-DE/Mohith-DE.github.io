from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model): 
    user= models.OneToOneField(User, on_delete=models.CASCADE) 
    image= models.ImageField(default='default.jpg', upload_to='profile_pics') 

    def __str__(self): 
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs): # Override the save method to resize the image
        super().save(*args, **kwargs)  # Call the original save method

        imp = Image.open(self.image.path) 
        if imp.height > 300 or imp.width > 300:
            output_size = (300, 300) 
            imp.thumbnail(output_size) # Save the resized image
            imp.save(self.image.path)

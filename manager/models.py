from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Portfolio(models.Model):
    category_choice=[
        ("Weddings",'weddings'),
        ("Engagements",'engagements'),
        ("Portraits",'portraits'),
    ]
    category = models.CharField(max_length=30, choices=category_choice)
    image = CloudinaryField("image", folder='TolsVisual/portfolio')

    def __str__(self):
        return f"{self.category} - {self.image}"

class Review(models.Model):
    name = models.CharField(max_length=256)
    image = CloudinaryField("image", folder='TolsVisual/reviews', blank=True, null=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Client(models.Model):
    category_choice = [
        ("Weddings", 'weddings'),
        ("Engagements", 'engagements'),
        ("Portraits", 'portraits'),
    ]
    category = models.CharField(max_length=30, choices=category_choice)
    name= models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"
class ClientImage(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField("image", folder="TolsVisual/clients")  # Set base folder

    def save(self, *args, **kwargs):
        # Ensure the image is stored in the correct subfolder
        if self.image and hasattr(self.image, 'public_id'):
            self.image.public_id = f"TolsVisual/clients/{self.client.name}/{self.image.public_id.split('/')[-1]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.client.name}"

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}"


class Home(models.Model):
    text = models.TextField()
    image_1 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_2 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_3 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_4 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_5 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_6 = CloudinaryField("image", folder="TolsVisual/home_page")
    image_7 = CloudinaryField("image", folder="TolsVisual/home_page")

    def save(self, *args, **kwargs):
        if Home.objects.exists() and not self.pk:
            raise ValueError("There can only be one Home instance.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "home details"

class About(models.Model):
    text = models.TextField()
    image = CloudinaryField('imaage', folder="TolsVisual/about")

    def __str__(self):
        return "about details"
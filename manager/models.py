from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Portfolio(models.Model):
    category_choice=[
        ("Weddings",'weddings'),
        ("Engagements",'engagements'),
        ("Portraits",'portraits'),
        ("Children and Family", "children and family"),
        ("Products and Lifestyle", "products and lifestyle")
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
        ("Children and Family", "children and family"),
        ("Products and Lifestyle","products and lifestyle")
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
    image_1 = CloudinaryField("image_1", folder="TolsVisual/home_page")
    image_2 = CloudinaryField("image_2", folder="TolsVisual/home_page")
    image_3 = CloudinaryField("image_3", folder="TolsVisual/home_page")
    image_4 = CloudinaryField("image_4", folder="TolsVisual/home_page")
    image_5 = CloudinaryField("image_5", folder="TolsVisual/home_page")
    image_6 = CloudinaryField("image_6", folder="TolsVisual/home_page")
    image_7 = CloudinaryField("image_7", folder="TolsVisual/home_page")
    wedding_img= CloudinaryField("wedding_image", folder="TolsVisual/home_page", null=True)
    portrait_img = CloudinaryField("portrait_image", folder="TolsVisual/home_page", null=True)
    engagement_img = CloudinaryField("engagement_image", folder="TolsVisual/home_page", null=True)

    def save(self, *args, **kwargs):
        if Home.objects.exists() and not self.pk:
            raise ValueError("There can only be one Home instance.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "home details"

class About(models.Model):
    text = models.TextField()
    top_image = CloudinaryField('top_image', folder="TolsVisual/about", null=True)
    main_img = CloudinaryField('main_img', folder="TolsVisual/about", null=True)

    def __str__(self):
        return "about details"
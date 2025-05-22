from django.db import models
from django.urls import reverse


class Room(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def get_api_url(self):
        return reverse("room-detail", kwargs={"slug": self.slug})

class Image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=255, blank=True)

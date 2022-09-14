from django.db import models

# Create your models here.
class Follower(models.Model):
    follower_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    user_link = models.CharField(max_length=1024, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.follower_id


class SearchOLXLink(models.Model):
    follower = models.ForeignKey(Follower, on_delete=models.CASCADE, related_name='olx_follower')
    olx_user_link = models.CharField(max_length=2500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.olx_user_link

class Product (models.Model):
    link = models.ForeignKey(SearchOLXLink, on_delete=models.CASCADE, related_name='product_link')
    follower = models.ForeignKey(Follower, on_delete=models.CASCADE, related_name='product_follower')
    title = models.CharField(max_length=255, blank=True)
    order_id = models.CharField(max_length=255, blank=True)
    order_link = models.CharField(max_length=2500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

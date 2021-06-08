from django.db import models

class Shows(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    network = models.CharField(max_length=45, default = "none")

# class Networks(models.Model):
#     name = models.CharField(max_length=45)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


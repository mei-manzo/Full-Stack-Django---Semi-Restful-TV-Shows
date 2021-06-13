from django.db import models

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "TV Show title should be at least 2 characters"
        if len(postData['description']) < 10:
            errors["description"] = "TV Show description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "TV Show description should be at least 3 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    network = models.CharField(max_length=45, default = "none")
    objects = ShowsManager()






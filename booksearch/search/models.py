from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)    
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)    
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):    
    name = models.CharField(max_length=20)
    biography = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ManyToManyField('Publisher')
    publication_date = models.DateField()
    headshot = models.ImageField(upload_to='book_headshots')
    summary = models.TextField(max_length=300,null=True)
    
    def __str__(self):
        return self.title

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="blog/")
    first = models.BooleanField(default=False)

    def is_first(self):
        if not Blog.objects.filter(first=True):
            return True

    def save(self, *args, **kwargs):
        self.first = self.is_first()
        return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    images = models.ImageField(upload_to="about/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def is_check(self):
        if About.objects.all().count() >= 2:
            self.is_active = False
        return self.is_active

    def save(self, *args, **kwargs):
        self.is_active = self.is_check()
        return Super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Contact(models.Model):
    profile_picture = models.ImageField(upload_to="profile/", null=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.address


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    choosen_blog = models.ManyToManyField(Blog, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date"]

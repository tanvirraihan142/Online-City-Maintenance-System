from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Catogery(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # slug = models.SlugField(allow_unicode=True, unique=True)
    # description = models.TextField(blank=True, default='')
    # description_html = models.TextField(editable=False, default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]


# COLOR_CHOICES = (
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )

class Post(models.Model):
   # catogery = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    catogery = models.ForeignKey(Catogery, related_name="post", null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    street = models.CharField(max_length=100, default='', blank=True, null=True)
    city = models.CharField(max_length=50, default='MIAMI', blank=True)
    state = models.CharField(max_length=50, default='FL', blank=True)
    zipcode = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='issuePics', default='default.jpg', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status, default='', related_name="post", null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    number_plate = models.CharField(max_length=50, default='', blank=True)
    make = models.CharField(max_length=50, default='', blank=True)
    model = models.CharField(max_length=50, default='', blank=True)
    color = models.CharField(max_length=50, default='', blank=True)

    pole_number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.content[:15]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()



class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

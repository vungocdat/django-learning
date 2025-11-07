from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # only values from 1 to 5
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')  # what happens to book when author is deleted
    bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)  # Harry Potter 1 -> harry-potter-1, will be created during the save()

#    def __str__(self):
#        return f'{self.title} ({self.rating})'

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

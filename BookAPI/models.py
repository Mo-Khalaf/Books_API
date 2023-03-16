
from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.full_name

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rent_fee = models.FloatField(blank=True, null=True)
    release_year = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'book'
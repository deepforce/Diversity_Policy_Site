from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class Policy(models.Model):

    POSSIBLE_TAGS = (
        ('diversity', 'Diversity'),
        ('admissions', 'Admissions'),
        ('enrollment', 'Enrollment'),
        ('faculty', 'Faculty'),
        ('student affairs', 'Student Affairs'),
        ('administrative', 'Administrative'),
        ('fees', 'Fees'),
        ('data measures', 'Data Measures'),
        ('international students', 'International Students'),
        ('academic standards', 'Academic Standards'),
        ('athletics', 'Athletics'),
        ('title ix', 'Title IX'),
        ('accreditation', 'Accreditation')
    )

    title = models.TextField(blank=True)
    school = models.CharField(max_length=255)
    department = models.TextField(blank=True, null=True)
    administrator = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True)
    city = models.TextField(blank=True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    link = models.TextField(blank=True)
    published_date = models.DateField(blank=True, null=True)
    tags = models.CharField(choices=POSSIBLE_TAGS, max_length=255, null=True)
    abstract = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True)
    search_vector = SearchVectorField(null=True)
    
    class Meta(object):
        
        indexes = [GinIndex(fields=['search_vector'])]

    def publish(self):
        self.save()

    def __str__(self):
        return self.title



# Customized User Model
class User(AbstractUser):
  ROLES_CHOICES = (
      (1, 'content_writer'),
      (2, 'content_manager'),
      (3, 'supervisor'),
      (4, 'admin'),
  )

  roles = models.PositiveSmallIntegerField(choices=ROLES_CHOICES, default=4)

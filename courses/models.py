from django.db import models
from django.contrib.auth.models import User

from .fields import OrderField


class Subject(models.Model):
    class Meta:
        ordering = ["title"]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, unique=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        ordering = ["-created"]

    owner = models.ForeignKey(
        User, related_name="courses_created", on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, related_name="courses", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=["course"])

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

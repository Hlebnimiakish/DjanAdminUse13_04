from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    def __str__(self):
        return self.firstname


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages_number = models.IntegerField()
    student_id = models.OneToOneField(Student, on_delete=models.SET_NULL, primary_key=False, null=True, blank=True)
    def __str__(self):
        return self.title
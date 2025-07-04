from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_author = models.CharField(max_length=200)
    project_detail = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.score
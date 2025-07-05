from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_author = models.CharField(max_length=200)
    project_detail = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def average_score(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()
        return 0

    def __str__(self):
        return self.project_name

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(1), 
                    MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.score)
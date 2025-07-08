from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# 프로젝트 클래스
class Project(models.Model):
    # 프로젝트 이름
    project_name = models.CharField(max_length=200)
    # 프로젝트 제작자
    project_author = models.CharField(max_length=200)
    # 프로젝트 상세 내용
    project_detail = models.TextField()
    # 프로젝트 생성 날짜
    pub_date = models.DateTimeField('date published', default=timezone.now)

    # 평균 점수 계산 함수
    def average_score(self):
        # Rating 클래스에서 점수들을 받아옴 
        ratings = self.rating_set.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()
        return 0

    def __str__(self):
        return self.project_name

# 유저가 매긴 점수 클래스
class Rating(models.Model):
    # 어떤 프로젝트에 대한 점수인가 참조하기 위함
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # 1~5점 사이의 점수
    score = models.IntegerField(
        validators=[MinValueValidator(1), 
                    MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.score)
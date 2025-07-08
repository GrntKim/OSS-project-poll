from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # 프로젝트 리스트
    path('', views.IndexView.as_view(), name='index'),
    # 프로젝트 내용
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 프로젝트 평가 결과
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 프로젝트 평가
    path('<int:project_id>/rate/', views.rate, name='rate'),
]
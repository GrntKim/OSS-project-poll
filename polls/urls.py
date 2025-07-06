from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('<int:project_id>/results/', views.results, name='results'),
    path('<int:project_id>/rate/', views.rate, name='rate'),
]
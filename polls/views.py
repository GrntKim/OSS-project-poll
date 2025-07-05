from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Project

def index(request):
    latest_project_list = Project.objects.order_by('-_pub_date')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'polls/index.html', context)

def detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'polls/detail.html', {'project': project})

def results(request, project_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % project_id)

def vote(request, project_id):
    return HttpResponse("You're voting on project No %s." % project_id)
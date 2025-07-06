from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Project, Rating

def index(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'polls/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'polls/detail.html', {'project': project})

def results(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'polls/results.html', {'project': project})

def rate(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    try:
        score = int(request.POST['choice'])
    except (KeyError, ValueError):
        return render(request, 'polls/detail.html', {
            'project': project,
            'error_message': "점수를 선택하세요.",
        })
    else:
        Rating.objects.create(project=project, score=score)
        return HttpResponseRedirect(reverse('polls:results', args=(project.id,)))
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project, Rating

# 프로젝트 리스트 뷰
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_project_list'
    
    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

# 프로젝트 내용 뷰
class DetailView(generic.DetailView):
    model = Project
    template_name = 'polls/detail.html'

# 프로젝트 결과 뷰 
class ResultsView(generic.DetailView):
    model = Project
    template_name = 'polls/results.html'

# 프로젝트 평가
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
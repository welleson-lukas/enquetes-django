from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questao, Choice

# Get questions and display them
def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detalhes(request, questao_id):
  try:
    questao = Questao.objects.get(pk=questao_id)
  except Questao.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'questao': questao})

# Get question and display results
def resultados(request, questao_id):
  questao = get_object_or_404(Questao, pk=questao_id)
  return render(request, 'polls/results.html', {'questao': questao})

# Vote for a question choice
def vote(request, questao_id):
    # print(request.POST['choice'])
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        selected_choice = questao.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': questao,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votos += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('enquete:resultados', args=(questao.id,)))

def resultadosData(request, obj):
    votodata = []

    questao = Questao.objects.get(id=obj)
    votos = questao.choice_set.all()

    for i in votos:
        votodata.append({i.choice_text: i.votos})
    return JsonResponse(votodata, safe=False)
from django.http import HttpResponse, Http404, JsonResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    response = {}
    response['question'] = question.question_text
    response['choices'] = []
    for choice in question.choice_set.all():
        response['choices'].append(choice.choice_text)
    print(response)
    return JsonResponse(response)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
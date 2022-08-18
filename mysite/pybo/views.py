from django.http import HttpResponse

from pybo.models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
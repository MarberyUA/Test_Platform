from django.forms import ModelForm
from .models import *


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['test_topic', 'description']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question']


class PossibleAnswerForm(ModelForm):
    class Meta:
        model = PossibleAnswer
        fields = ['answer', 'right_answer']

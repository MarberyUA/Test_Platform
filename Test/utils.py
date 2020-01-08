from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, reverse

from .models import *


def is_minimum(questions):
    i = 0

    try:
        questions_amount = len(questions)

        for question in questions:
            answers = PossibleAnswer.objects.filter(question_id=question.id)
            right_answers = answers.filter(right_answer=True)
            if len(answers) == 4 and len(right_answers) == 1:
                i += 1

    except:
        questions_amount = 1
        answers = PossibleAnswer.objects.filter(question_id=questions.id)
        right_answers = answers.filter(right_answer=True)
        if len(answers) == 4 and len(right_answers) == 1:
            i += 1

    if i == questions_amount:
        return True
    else:
        return False


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)

        if self.model.__name__ == 'Question':
            is_right_answers = is_minimum(obj)
        else:
            is_right_answers = None

        return render(request, self.template, context={'obj': obj, 'right_answers': is_right_answers})


class ObjectCreateMixin:
    form_class = None
    template = None

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            new_object.created_by = request.user
            new_object.save()
            return redirect(reverse('test_detail_url', kwargs={'id': new_object.id}))


class AdditionObjectCreateMixin:
    form_class = None
    template = None

    def get(self, request, id):
        form = self.form_class()
        if self.form_class.__name__ == 'QuestionForm':
            obj = Test.objects.get(id=id)
        else:
            obj = Question.objects.get(id=id)
        return render(request, self.template, context={'form': form, 'obj': obj})

    def post(self, request, id):
        bound_form = self.form_class(request.POST)
        if self.form_class.__name__ == 'QuestionForm':
            if bound_form.is_valid():
                new_object = bound_form.save()
                test = Test.objects.get(id=id)
                new_object.test = test
                new_object.save()
                return redirect(reverse('questions_list_url', kwargs={'id': test.id}))

        elif self.form_class.__name__ == 'PossibleAnswerForm':
            question = Question.objects.get(id=id)
            answers_amount = PossibleAnswer.objects.filter(question_id=question.id)
            if bound_form.is_valid():
                new_object = bound_form.save()
                question = Question.objects.get(id=id)
                new_object.question = question
                new_object.save()
                return redirect(reverse('question_detail_url', kwargs={'id': question.id}))

        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    form_class = None
    model = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        form = self.form_class(instance=obj)
        return render(request, self.template, context={'obj': obj, 'form': form})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.form_class(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            if self.model.__name__ == 'Test':
                return redirect(reverse('test_detail_url', kwargs={'id': obj.id}))
            elif self.model.__name__ == 'PossibleAnswer':
                return redirect(reverse('question_detail_url', kwargs={'id': obj.question_id}))
            else:
                return redirect(reverse('questions_list_url', kwargs={'id': obj.test_id}))
        return render(request, self.template, context={'form': bound_form, 'obj': obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_link = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        return render(request, self.template, context={'obj': obj})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        obj.delete()
        if self.model.__name__ == 'Question':
            return redirect(reverse('questions_list_url', kwargs={'id': obj.test_id}))

        elif self.model.__name__ == 'PossibleAnswer':
            return redirect(reverse('question_detail_url', kwargs={'id': obj.question_id}))
        else:
            return redirect(self.redirect_link)

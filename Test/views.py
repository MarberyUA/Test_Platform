from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
from .utils import *
from django.db.models import Q


# Create your views here.


class TestsList(View):
    def get(self, request):
        searching_query = request.GET.get('search', None)
        if searching_query:
            tests = Test.objects.filter(Q(test_topic__icontains=searching_query))
        else:
            tests = Test.objects.all()
        return render(request, 'tests_list.html', context={'tests': tests})

    def post(self, request):
        marks = TestMarks.objects.filter(user_id=request.user)
        tests = [Test.objects.get(id=i.test_id) for i in marks]
        return render(request, 'tests_list.html', context={'tests': tests})


class QuestionsList(View):
    def get(self, request, id):
        test = Test.objects.get(id=id)
        questions = Question.objects.filter(test_id=id)
        return render(request, 'questions_list.html', context={'questions': questions, 'test': test})


class TestDescription(View):
    def get(self, request, id):
        test = Test.objects.get(id=id)

        try:
            user_assessment = TestMarks.objects.get(test_id=id, user_id=request.user.id).mark
        except:
            user_assessment = 0

        obj_questions = Question.objects.filter(test_id=id)
        comments = Comment.objects.filter(test_id=id)
        verified = is_minimum(obj_questions)
        if not verified:
            verified_context = 'Status: Test does not have 5 questions or ' \
                               'test questions have many right answers or do not have it  ' \
                               'Wait while creator edit the questions.'
        else:
            verified_context = None
        return render(request, 'test_detail.html', context={'test': test, 'comments': comments,
                                                            'questions': obj_questions,
                                                            'assessment': user_assessment,
                                                            'verified': verified,
                                                            'verified_context': verified_context}
                      )

    def post(self, reqeust, id):
        test = Test.objects.get(id=id)
        if reqeust.POST.get('comment', None) == '' or reqeust.POST.get('comment', None) == ' ':
            error = 'You must write something to add a comment'
            return render(reqeust, 'test_detail.html', context={'test': test, 'error': error})
        else:
            comment = Comment.objects.create(comment=reqeust.POST.get('comment', None),
                                             test=test,
                                             created_by=reqeust.user)
            success = 'You have added the comment!'
            return redirect(reverse('test_detail_url', kwargs={'id': id}))


class TestPass(View):
    def get(self, request, id):
        test = Test.objects.get(id=id)
        questions = Question.objects.filter(test_id=id)
        return render(request, 'test_pass.html', context={'questions': questions, 'test': test})

    def post(self, request, id):
        test = Test.objects.get(id=id)
        questions = Question.objects.filter(test_id=id)
        values = request.POST.getlist('answer')
        if len(values) < len(questions):
            error = 'Match all answers!'
            return render(request, 'test_pass.html', context={'error': error, 'test': test})
        else:
            questions = Question.objects.filter(test_id=test.id)
            mark = 0
            i = 0
            for obj in questions:
                answers = PossibleAnswer.objects.filter(question_id=obj.id)
                for answer in answers:
                    if (answer.right_answer == 1) and (answer.answer == values[i]):
                        mark += 1
                    i += 1

            percent_mark = mark / len(questions) * 100
            try:
                user_mark = TestMarks.objects.get(user_id=request.user.id, test_id=test.id)
                user_mark.mark = percent_mark
                user_mark.save()
            except:
                TestMarks.objects.create(test=test, mark=percent_mark, user=request.user)
                test.number_passes += 1
                test.save()

            return render(request, 'result.html', context={'test': test, 'mark': mark, 'percent_mark': percent_mark})


class TestCreate(ObjectCreateMixin, View):
    form_class = TestForm
    template = 'test_create.html'


class TestUpdate(ObjectUpdateMixin, View):
    form_class = TestForm
    model = Test
    template = 'test_edit.html'


class TestDelete(ObjectDeleteMixin, View):
    model = Test
    template = 'test_delete.html'
    redirect_link = 'main_page_url'


class QuestionCreate(AdditionObjectCreateMixin, View):
    form_class = QuestionForm
    template = 'question_create.html'


class QuestionDetail(ObjectDetailMixin, View):
    model = Question
    template = 'question_detail.html'


class QuestionUpdate(ObjectUpdateMixin, View):
    form_class = QuestionForm
    model = Question
    template = 'question_edit.html'


class QuestionDelete(ObjectDeleteMixin, View):
    model = Question
    template = 'question_delete.html'


class PossibleAnswerCreate(AdditionObjectCreateMixin, View):
    form_class = PossibleAnswerForm
    template = 'possible_answer_create.html'


class PossibleAnswerEdit(ObjectUpdateMixin, View):
    form_class = PossibleAnswerForm
    model = PossibleAnswer
    template = 'possible_answer_edit.html'


class PossibleAnswerDelete(ObjectDeleteMixin, View):
    model = PossibleAnswer
    template = 'possible_answer_delete.html'

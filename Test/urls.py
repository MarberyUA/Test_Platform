from django.urls import path
from .views import *

urlpatterns = [
    path('', TestsList.as_view(), name='main_page_url'),
    path('test/create/', TestCreate.as_view(), name='test_create_url'),
    path('test/<int:id>/details/', TestDescription.as_view(), name='test_detail_url'),
    path('test/<int:id>/questions/', QuestionsList.as_view(), name='questions_list_url'),
    path('question/<int:id>/edit', QuestionUpdate.as_view(), name='question_edit_url'),
    path('question/<int:id>/delete', QuestionDelete.as_view(), name='question_delete_url'),
    path('test/<int:id>/create_question/', QuestionCreate.as_view(), name='create_question_url'),
    path('test/<int:id>/pass/', TestPass.as_view(), name='test_pass_url'),
    path('test/<int:id>/create_possible_answer/', PossibleAnswerCreate.as_view(), name='possible_answer_create_url'),
    path('test/question/<int:id>/detail/', QuestionDetail.as_view(), name='question_detail_url'),
    path('test/<int:id>/edit/', TestUpdate.as_view(), name='test_edit_url'),
    path('test/<int:id>/delete/', TestDelete.as_view(), name='test_delete_url'),
    path('possible_answer/<int:id>/edit', PossibleAnswerEdit.as_view(), name='possible_answer_edit_url'),
    path('possible_answer/<int:id>/delete', PossibleAnswerDelete.as_view(), name='possible_answer_delete_url'),
]
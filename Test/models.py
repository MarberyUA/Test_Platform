from django.db import models
from django.shortcuts import reverse
import accounts
import accounts.models
from Test_Platform import settings

# Create your models here.


class Test(models.Model):
    """Main model on which are based other models from this app"""

    test_topic = models.CharField(max_length=50)
    number_passes = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, default='No description')
    date_pub = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='creator')

    def __str__(self):
        return self.test_topic


    class Meta:
        ordering = ['-date_pub']


class Question(models.Model):
    question = models.TextField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question


class PossibleAnswer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    right_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

    def get_detail_url(self):
        question = Question.objects.get(id=self.question_id)
        return reverse('question_detail_url', kwargs={'id': question.id})

    def get_test_questions_url(self):
        question = Question.objects.get(id=self.question_id)
        return reverse('questions_list_url', kwargs={'id': question.test_id})

    def get_edit_url(self):
        return reverse('possible_answer_edit_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('possible_answer_delete_url', kwargs={'id': self.id})


class Comment(models.Model):
    """"""

    comment = models.TextField(max_length=1000)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class TestMarks(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    mark = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
from django import template
from accounts.models import User
from Test.models import Test, Question, PossibleAnswer, TestMarks
from django.templatetags.static import static
from Test_Platform.settings import STATIC_URL

register = template.Library()

@register.filter()
def get_user_detail(id, num):
    user = User.objects.get(id=id)
    if not user.profile_photo:
        photo = STATIC_URL + 'pictures/no-avatar.jpg'
    else:
        photo = user.get_absolute_image_url
    user_attrs = {0: user.email, 1: user.username, 2: photo,
                  3: user.birthday}

    result = user_attrs[num]
    return result


@register.filter()
def get_answers(question):
    answers = PossibleAnswer.objects.filter(question_id=question.id)
    return answers

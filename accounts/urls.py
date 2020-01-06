from django.urls import path
from accounts.views import *

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up_url'),
    path('<int:id>/account_detail/', UserDetail.as_view(), name='user_detail_url'),
    path('<int:id>/account_detail/update/', UserDetailUpdate.as_view(), name='user_details_update_url'),
    path('password_reset/', ChangeUserDetails.as_view(), name='password_reset_url' ),
    path('password_reset_done/', ChangeUserDetailsDone.as_view(), name='password_reset_done_url'),
]
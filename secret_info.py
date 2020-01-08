from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()

# db secret info

# db user
DB_USER = ''
# db user password
DB_USER_PASSWORD = ''

# vk auth

# your oauth2 application id from VK
SOCIAL_AUTH_VK_OAUTH2_KEY = ''

# your oauth2 secret key from VK APP
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''

SOCIAL_AUTH_VK_APP_USER_MODE = 2
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# google social auth https://github.com/MarberyUA/Test_Platform/tree/master/readme_screenshots

# your oauth2 application id from GOOGLE
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''

# your oauth2 secret key from GOOGLE APP
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# email secret info


EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True

# for future register verification




# Test_Platform

The first step you should do the git clone!
```git
git clone /repository-link/
```

# The you will have such dirs in base project dir:

accounts/
---
media/
---
static/
---
templates/
---
Test/
---
Test_Platform/
---
manage.py
---
requirements/
---
secret_info.py/
---

Firstly go to secret_info.py and change such variables:

Set up your db user name:
```python
1. DB_USER = ''
```
Set up your db user password:
```python
2. DB_USER_PASSWORD = ''
```
Set up your oauth2 application id from VK:
```python
3. SOCIAL_AUTH_VK_OAUTH2_KEY = ''
```
Set up your oauth2 secret key from VK APP:
```python
4. SOCIAL_AUTH_VK_OAUTH2_SECRET = ''
```
Set up your oauth2 application id from GOOGLE:
```python
5. SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
```
Set up your oauth2 secret key from GOOGLE APP:
```python
6. SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
```

Secondly go to Test_Platform/settings.py and write database name:
```python
from secret_info import DB_USER, DB_USER_PASSWORD

DATABASES = {
    'default': {
        # db name
        'NAME': '',
        'ENGINE': 'django.db.backends.mysql',
        'USER': DB_USER,
        'PASSWORD': DB_USER_PASSWORD,
        'HOST': 'localhost',
    }
}
```

Then do the migrate for your database:
```python
python manage.py migrate
```

Also to get started and see what project can provide we need to load prepared data with such commands:
```python
python manage.py loaddata accounts/fixtures/initial_data.json
python manage.py loaddata Test/fixtures/initial_data.json
```

# Then you must do this and enjoy the project:
```python
python manage.py runserver
```

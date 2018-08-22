
# Learning Django



# Inital generator notes:
- `django-admin startproject mysite` creates templates
- `python manage.py makemigrations polls` migtrate app; basically update django about changes to model
- `python manage.py sqlmigrate polls 0001` provides/logs sql operations from app
- `python manage.py migrate` creates model tables in database
- create superuser: `python manage.py createsuperuser`
- admin login: http://127.0.0.1:8000/admin/
  - username: admin
  - email: admin@website.com
  - password: password123


### Not expected behavior
- continue testing from [here](https://django.readthedocs.io/en/1.11.x/intro/tutorial05.html)
- [repos to compare against](https://www.google.co.in/search?newwindow=1&ei=wNF9W5TnHMy_rQGY16uoBg&q=first+django+app+github+choices+not+displaying&oq=first+django+app+github+choices+not+displa&gs_l=psy-ab.3.0.33i21k1j33i160k1l2.142780.146685.0.148348.19.19.0.0.0.0.179.1989.11j8.19.0....0...1c.1.64.psy-ab..0.18.1907...0i22i30k1j33i22i29i30k1.0.40pE1HtJnyc)



## Setup:
- `cd` into the directory and run `python manage.py runserver`
- ~~VIrutal env: https://docs.djangoproject.com/en/2.1/howto/windows/~~
- ~~run `workon learningDjangoVirtualEnv` to use virtual env~~


Reference:
- https://docs.djangoproject.com/en/2.1/intro/tutorial01/
- Use appropriate version of documentation:
  - https://django.readthedocs.io/en/1.11.x/intro/tutorial01.html


### Update:
- The django version running on my machine is 1.1 and not 2.1
- Documentation i'm following is now [this](https://django.readthedocs.io/en/1.11.x/intro/tutorial01.html) and not [this](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) from earlier
- Realized the problem when I couldn't import include and path from django config
- The the server points to http://127.0.0.1:8000/polls/
-

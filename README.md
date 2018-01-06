COMP3207 - Cloud Application Development
Group Coursework


Google Cloud SQL
MySQL
instance ID: instance1
IP address: 35.224.177.65
user: root
password: root

Tutorial for Social Auth: https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html

If experience error "Site matching query does not exist.", here's the solution:
(1) python manage.py shell
(2) from django.contrib.sites.models import Site
(3) Site.objects.create(name='localhost', domain='localhost')
(4) Site.objects.create(name='comp3207-travel-planner-189701.appspot.com', domain='comp3207-travel-planner-189701.appspot.com')

or go to /admin/ panel and add Site
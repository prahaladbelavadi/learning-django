from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',views.IndexView.asView(), name='index'),
    # example: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.asView(), name='detail'),
    # example: /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.asView(), name='results'),
    # example: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

from django.conf.urls import url

from . import views

app_name = 'site'

urlpatterns = [
    # ex: /site/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /site/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /site/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /site/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /site/giphy/cat/
    url(r'^giphy/(?P<giphy_search>[a-zA-Z+]+)/$', views.giphy, name='giphy'),
    # ex: /site/giphy/tally/hits/
    url(r'^giphy/tally/hits/$', views.tally, name='tally'),

    url(r'^tableau/sample/$', views.tableau, name='tableau'),

    url(r'^imdb/top/$', views.imdb, name='imdb'),

    url(r'^survey/printall/$', views.post_request, name='callback'),

    url(r'^socrata-app/callback/$', views.socrataCallback, name='socrataCallback'),

    url(r'^socrata-app/detail/$', views.socrataDetail, name='socrataDetail'),

  #  url(r'^giphy/movie/(?P<moviegiphy_search>[a-zA-Z+]+)/$', views.moviegiphy, name='moviegiphy'),
]

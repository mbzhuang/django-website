import json
import urllib2
import pandas as pd

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question
from .models import Choice
from .models import Hits
from .models import TopMovies
from .models import Key
from imdbpie import Imdb
from nltk.corpus import stopwords
import giphypop
from numpy.random import RandomState
from classproject.settings import TWITTER_APP_KEY, TWITTER_APP_SECRET,TWITTER_OAUTH_TOKEN,TWITTER_OAUTH_TOKEN_SECRET
from django.views.decorators.csrf import csrf_exempt
from mlModel import mlModel

knn = mlModel()

class IndexView(generic.ListView):
    template_name = 'site/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'site/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'site/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'site/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('site:results', args=(question.id,)))


def giphy(request, giphy_search):
    giphy_json = []
    soup = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q="+ giphy_search + "&api_key=dc6zaTOxFJmzC").read()
    parsed_json  = json.loads(soup)
    counter = 0
    for i in parsed_json['data']:
	giphy_json += [(str(counter),str(i['images']['fixed_width']['url']))]
	counter += 1

    # if not found, create a new one with hits being 1
    hit, created = Hits.objects.get_or_create(name=giphy_search, defaults={"name": giphy_search, "hits":1})
    if not created:
        hit.hits += 1
        hit.save()
    return render(request, 'site/giphy.html', {'giphy': giphy_json})

def tally(request):
    return render(request, 'site/tally.html', {'hits': Hits.objects.all()})

def tableau(request):
   return render(request, 'site/tableau.html')


def imdb(request): # Populate the database when it is visited for the first time
    if len(TopMovies.objects.all())<1:
        df = pd.read_csv('imdb.csv', sep='\t', encoding='utf-8')
        movie_instances = []
        for index, movie in df.iterrows():
            movie_instances += [
                TopMovies(
                    Title = movie['Title'],
                    Rank = movie['Rank'] + 1,
                    Released = movie['Released'],
                    Poster = movie['Poster'],
                    url = movie['url'],
                    Year = movie['Year'],
                    Genre = movie['Genre'],
                    Awards = movie['Awards'],
                    imdbRating = movie['imdbRating'],
                    gross_revenue = movie['gross'],
                    Actors = movie['Actors'],
                    Director = movie['Director'],
                    Plot = movie['Plot']
                )
            ]
        TopMovies.objects.bulk_create(movie_instances)
    return render(request, 'site/imdb.html', {'movies': TopMovies.objects.all()})

@csrf_exempt
def post_request(request):
#    if request.method != 'POST': 
#        return HttpResponse("wrong request") 
#    else:
#        mykey = request.POST.get('key', '')
#        Key.objects.all().delete()
#        data = { 'email' : 'jason.feiwang@gmail.com', 'key': mykey}
#        response = requests.post('https://peaceful-badlands-42479.herokuapp.com/site/survey/verification/', data=data)
#        Key.objects.get_or_create(Key=mykey)

    if request.POST.get('type') != 'coordinates':
        return HttpResponse("wrong request")
    else:
        lat = request.POST.get('latitude', '')
        lon = request.POST.get('longitude', '')
        predCrime = knn.predict(lat, lon)
        score = knn.score
        return HttpResponse("The predicted crime at this location is '%s' and the model accuracy is %.2f" %(predCrime, score))

def socrataCallback(request):
    pass

def socrataDetail(request):
    pass


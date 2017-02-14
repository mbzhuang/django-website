from django.core.management.base import BaseCommand, CommandError
#from website.models import TWITTERTWEET, TWITTERUSER
import os

TWITTER_APP_KEY = os.environ.get('TWITTER_APP_KEY', '')
TWITTER_APP_SECRET = os.environ.get('TWITTER_APP_SECRET', '')
TWITTER_OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', '')
TWITTER_OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', '')
class Command(BaseCommand):
    help = 'pull in a few tweets based on a query'

    def add_arguments(self, parser):
        parser.add_argument('query', nargs='+', type=int)

    def handle(self, *args, **options):
    #    for q in options['query']:
    #        try:
    #            # Do Query Logic Here
    #        except Exception as e:
    #            raise CommandError(e)

            self.stdout.write(self.style.SUCCESS('SuccessQ'))

# coding=utf-8

# sudo easy_install python-twitter
import twitter
import json

    # inicializamos nuestra cuenta de twitter => https://apps.twitter.com/
api = twitter.Api(consumer_key='GzJFq7AM53WE2MNUOpGhu1xqI',
    consumer_secret='wVl1DtHBLglwiWLKFhCbuegyd7PdD799kuEihy24TdjgDr27UA',
    access_token_key='4428194794-2UfPUuwSftc7VYchW7UTPHUfCZCOkkte9nxHvKH',
    access_token_secret='APJruzWG3R3X6QoGwCyLo3hZfzAzAHbQ1CwEG1E6bq83X')
  
    # Comprueba que la cuenta es correcta  
# json.dumps(api.VerifyCredentials())

statuses = api.GetUserTimeline(screen_name="eldiarioes")
print [s.text for s in statuses]
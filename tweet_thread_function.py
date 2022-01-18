import random
import tweepy

def make_tweet(client_obj, list_threads):
    f = list_threads[random.randint(0,len(list_threads))][0]

    #print(str(f)) #debugging

    response = client_obj.create_tweet(text=str(f))
    return response

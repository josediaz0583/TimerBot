
# coding: utf-8

# In[1]:


import tweepy
import time


# In[2]:


# Twitter API Keys
consumer_key = "r4b58sAz2lqEQZj3DpMkc0ibi"
consumer_secret = "kHH72T9XrpzGHJAgdVRZAlaRLEeDPm0AujM2pdNQpU4uhVxgUJ"
access_token = "975021712332017665-beqYO52oVSm94MsENtMoMY0XrJc9x1F"
access_token_secret = "5a2BWlPfRKxONfShepLlj2farPcNnkSdH9Kz9ODCR45mu"


# In[3]:


# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[ ]:


# Send tweets every 60 Seconds to your homepage
tweet_num = 1
while tweet_num < 6:
   api.update_status("Tweet Number :" + str(time.ctime()) + " counter: " + str(tweet_num))
   tweet_num = tweet_num + 1
   time.sleep(60)


# Reddit-Hourly-Post-On-twitter-
Twitter bot posting trending media from various animal related subreddits. 

How to set-up the bot?
- Set up a creds.py file and copy your api keys. 
 	```python
  CONSUMER_KEY = ""
  CONSUMER_SECRET =""
  ACCESS_TOKEN = ""
  ACCESS_TOKEN_SECRET = ""
  REDDIT_CLIENT_ID = ""
  REDDIT_CLIENT_SECRET = ""
  REDDIT_USER_AGENT = ""
  ``` 
  **DO NOT DISCLOSE THEM BY ANY MEAN** 
  
- Add subreddits to the subreddit_list array in **settings.py** as well as their associated tweet. 
- Append IDs of the post you'd like to remove from selection in the banned_post_list located in **settings.py**


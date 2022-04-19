-- *Note: The twitter api V2 has no endpoit for medias yet.*<br>
---*Note2: I decided to re-write the bot from scratch. it works, tho.*

## Reddit to twitter bot. 
*Twitter bot posting media from various subreddits.*

### Requirement: 
+ You need ffmpeg installed on your machine.
+ You need an access to the twitter Api V1. 



### Set-up: 
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
  
 ### In setting.py
- Add subreddits to the subreddit_list array as their associated tweet.
- You can also set-up a default tweet in case no body is specified.
- Append IDs of the post you'd like to remove from selection in the banned_post_list






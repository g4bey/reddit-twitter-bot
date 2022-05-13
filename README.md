## Reddit to twitter bot. 
*Twitter bot posting media from various subreddits.*

### Requirement: 
+ You need ffmpeg installed on your machine.
+ You need an access to the twitter Api V1. 


### Set-up: 
- Set up a creds.py file and copy your api keys. 
You can also use environement variables. 
```python
    twitter = {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
    }

    reddit = {
        "client_id" : "",
        "client_secret" : "",
        "user_agent" : ""
    }
``` 
  **DO NOT DISCLOSE THEM BY ANY MEAN** 
  
 - Define subreddit and their respective tweet.<br>
*If key values are left empty, `default_tweet` will be its value.*
```python
 subreddits = {
      subreddit1: This is a tweet.,
      subreddit2: ''
    }
```

- You can dynamically ban posts appending submission.id to banned_post[] 
```python
 banned_post = [
    u7vamm,
    u7wts1
 ]
```

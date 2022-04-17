"""Settings for the application.

fSTATE: the state of your program.
    / it helps alternating between subreddits

fPREVIOUS_POSTS: store the 400 previous posts.

fMEDIA_FOLDER: home of the downloaded medias.

banned_post_list: posts you want to ban.
    / often subreddit have pinned posts.
    / this won't affect the application
    / but that's a waste of ressource.

submission_to_fetch: submission you want to fetch.
    / Media will be indexed, not downloaded.
    / the script stops at the first
    / tweet posted.

subreddit_list: the list of subreddit to alternate with.
"""

fSTATE = ".program_state"
fPREVIOUS_POSTS = ".previous_posts"
fMEDIA_FOLDER = "media"

banned_post_list = ["hyts0n"]

submission_to_fetch = 10

subreddit_list = (
    ['aww', 'your hourly fluffbutt:'],
    ['furry_irl', 'your hourly husko:'],
    ['Unexpected', 'your hourly ask me:']
)
